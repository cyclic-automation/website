import pandas
import reflex as rx
import pandas as pd
import pdfplumber
import requests
import io
import re
from utils.data import process_df
from utils.emailer import send_email


class FormState(rx.State):
    form_data = {}
    df = pandas.DataFrame

    def handle_submit(self, form_data):
        if form_data['email_to']:
            send_email(email_to=form_data['email_to'],
                       df=self.df)
            return rx.toast.success("Email Sent", position="top-center")


class TabsState(rx.State):
    value = "tab_intro"

    def change_value(self, value):
        self.value = value


def intro() -> rx.Component:
    return rx.vstack(
        rx.heading("Introduction"),
        rx.text("""
        This page features a series of hypothetical demonstration projects showing the versatility of our automation solutions. 
        These examples use arbitrary data to give a sense of how we can help streamline your data processes. 
        Navigate through the tabs to see these concepts in action.
        """),
        justify="center",
        align="center",
        width="50%"
    )


def data_visualization() -> rx.Component:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    url = "https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/population-density-data-table.pdf"
    response = requests.get(url)
    pdf_file = io.BytesIO(response.content)
    pdf = pdfplumber.open(pdf_file)

    ca, tx, fl, ny = [], [], [], []
    pattern = r"\s+([\d,]+)\s+[\d,.]+\s+[\d]+\s+([\d,]+)\s+[\d,.]+\s+[\d]+\s+([\d,]+)"
    for page in pdf.pages[:-2]:
        text = page.extract_text().lower()
        ca_triplet = re.search("california" + pattern, text)
        tx_triplet = re.search("texas" + pattern, text)
        fl_triplet = re.search("florida" + pattern, text)
        ny_triplet = re.search("new york" + pattern, text)
        for i in [1, 2, 3]:
            ca.append(int(ca_triplet.group(i).replace(",", "")))
            tx.append(int(tx_triplet.group(i).replace(",", "")))
            fl.append(int(fl_triplet.group(i).replace(",", "")))
            ny.append(int(ny_triplet.group(i).replace(",", "")))

    states = [ca, tx, fl, ny]
    df = pd.DataFrame(states, columns=[str(2020 - 10 * i) for i in range(len(states[0]))])
    df["State"] = ["CA", "TX", "FL", "NY"]
    df = df.set_index("State")
    df.columns.name = "Year"
    df = df.reindex(columns=df.columns[::-1])

    df = df.map(lambda x: x * 1e-6)
    df = df.map(lambda x: round(x, 2))

    FormState.df = df

    return rx.vstack(
        rx.heading("Data Extraction & Visualization"),
        rx.text("""
                Here we extract US state population data from a PDF sourced from census.gov. 
                The data is first organized into a table for clarity, then visualized using a graph to highlight trends. 
                This process illustrates our ability to extract data from any document format and transform it into customized, meaningful insights.
                """),
        rx.spacer(),
        rx.heading("State Population Growth"),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="CA",
                             unit="M",
                             type_="monotone",
                             stroke=rx.color("blue"),
                             dot={"blue": rx.color("blue"), "fill": rx.color("blue", 4)}),
            rx.recharts.line(data_key="FL",
                             unit="M",
                             type_="monotone",
                             stroke=rx.color("red"),
                             dot={"blue": rx.color("red"), "fill": rx.color("red", 4)}),
            rx.recharts.line(data_key="NY",
                             unit="M",
                             type_="monotone",
                             stroke=rx.color("green"),
                             dot={"blue": rx.color("green"), "fill": rx.color("green", 4)}),
            rx.recharts.line(data_key="TX",
                             unit="M",
                             type_="monotone",
                             stroke=rx.color("purple"),
                             dot={"blue": rx.color("purple"), "fill": rx.color("purple", 4)}),
            rx.recharts.x_axis(data_key="Year",
                               label={"value": "Year", "position": "bottom"}),
            rx.recharts.y_axis(unit="M",
                               domain=[5, 40],
                               label={"value": "Population", "position": "left", "angle": -90}),
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.graphing_tooltip(),
            rx.recharts.legend(vertical_align="top",
                               layout="vertical",
                               align="right",
                               icon_type="square"),
            data=df.T.reset_index().to_dict("records"),
            margin={"top": 20, "right": 20, "left": 20, "bottom": 20},
            width=800,
            height=300,
        ),
        rx.data_table(
            data=df.reset_index().assign(Unit='Million (M)'),
            sort=True,

        ),
        rx.text("Population change for the four most populous US States."),
        rx.link("Source PDF: Census.gov",
                href="https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/population-density-data-table.pdf"),
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.control(
                        rx.input(
                            placeholder="Email Me The Data",
                            type="email",
                        ),
                        as_child=True,
                    ),
                    rx.form.submit(
                        rx.button("Send"),
                        as_child=True,
                    ),
                    direction="row",
                    justify="center"
                ),
                rx.flex(
                    rx.form.message(
                        "Invalid Email",
                        match="typeMismatch",
                    ),
                    justify="center"
                ),
                name="email_to",
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        justify="center",
        align="center",
    )


def data_format() -> rx.Component:
    process_df()
    contacts_df = pd.read_csv("data/contacts.csv")
    contacts_processed_df = pd.read_csv("data/contacts_processed.csv")
    contacts_rejected_df = pd.read_csv("data/contacts_rejected.csv")
    return rx.vstack(
        rx.heading("Data Cleansing & Formatting"),
        rx.text("""
        Here we start with a dataset of hypothetical (randomly generated) client information, filled with messy formatting and errors.
        The data is then cleansed, standardized, and obvious errors are automatically removed. 
        Entries requiring further human review are flagged and set aside.
        This example used a small dataset for demonstration purposes, but this algorithm can be used to organize immense datasets at a rapid pace. 
        """),
        rx.spacer(),
        rx.heading("Randomly Generated Client Data"),
        rx.data_table(
            data=contacts_df,
            pagination=True,
            search=True,
            sort=True,
        ),
        rx.text("""
                The table shows randomly generated client information. 
                This data is inputted with varying formats, and contains errors. 
                We will now format the data automatically:
                """),
        rx.spacer(),
        rx.spacer(),
        rx.heading("Processed Client Data"),
        rx.data_table(
            data=contacts_processed_df,
            sort=True,
        ),
        rx.text("""
                Client data of varying formats are standardized. 
                Any obviously correctable errors are automatically corrected.
                """),
        rx.spacer(),
        rx.heading("Rejected Client Data"),
        rx.data_table(
            data=contacts_rejected_df,
            sort=True,
        ),
        rx.text("""
                Client data containing ambiguous errors that could not be resolved automatically. 
                An extra column is added to explain exactly where the error is located. 
                This data is saved into a separate file to be reviewed by a human in its original format.
                """),
        justify="center",
        align="center"
    )


def examples() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Introduction", value="tab_intro"),
                    rx.tabs.trigger("Data Extraction & Visualization", value="tab_data_graph"),
                    rx.tabs.trigger("Data Cleansing & Formatting", value="tab_data_format"),
                    size="2",
                ),
                value=TabsState.value,
                on_change=lambda x: TabsState.change_value(x),
            ),

            rx.match(
                TabsState.value,
                ("tab_intro", intro()),
                ("tab_data_graph", data_visualization()),
                ("tab_data_format", data_format()),
                rx.text("Please Select")
            ),
            align="center",
            justify="center",
        ),
        width="80%",
    )
