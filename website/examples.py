import reflex as rx
import pandas as pd

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CAPOP,FLPOP,NYPOP,TXPOP&scale=left,left,left,left&cosd=1960-01-01,1960-01-01,1960-01-01,1960-01-01&coed=2023-01-01,2023-01-01,2023-01-01,2023-01-01&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b&link_values=false,false,false,false&line_style=solid,solid,solid,solid&mark_type=none,none,none,none&mw=3,3,3,3&lw=2,2,2,2&ost=-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999&mma=0,0,0,0&fml=a,a,a,a&fq=Annual,Annual,Annual,Annual&fam=avg,avg,avg,avg&fgst=lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4&transformation=lin,lin,lin,lin&vintage_date=2024-10-17,2024-10-17,2024-10-17,2024-10-17&revision_date=2024-10-17,2024-10-17,2024-10-17,2024-10-17&nd=1900-01-01,1900-01-01,1900-01-01,1900-01-01"
df = pd.read_csv(url)

df = df.set_index("DATE")
df.index.name = "YEAR"
df.columns = df.columns.map(lambda x: x.replace("POP", ""))
df.columns.name = "STATE"

df = df.rename(index=lambda x: x[:4])
df = df.map(lambda x: x * 1e3)
df = df.map(lambda x: x * 1e-6)
df = df.map(lambda x: round(x, 2))

df = df[df.index.astype(int) % 10 == 0]


# print(df)

class TabsState(rx.State):
    value = "tab_graph"

    def change_value(self, value):
        self.value = value


def intro() -> rx.Component:
    return rx.vstack(
        rx.text(""),
    )


def table() -> rx.Component:
    return rx.vstack(
        rx.heading("State Population"),
        rx.data_table(
            data=df.reset_index(),
            sort=True,
        ),
        rx.text("Population change for the four most populous US States"),
        align="center",
        justify="center",
        width="90%",
    )


def graph() -> rx.Component:
    return rx.vstack(
        rx.heading("State Population"),
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
            rx.recharts.x_axis(data_key="YEAR",
                               label={"value": "Year", "position": "bottom"}),
            rx.recharts.y_axis(unit="M",
                               label={"value": "Population", "position": "left", "angle": -90}),
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.graphing_tooltip(),
            rx.recharts.legend(vertical_align="top",
                               layout="vertical",
                               align="right",
                               icon_type="square"),
            data=df.reset_index().to_dict("records"),
            margin={"top": 20, "right": 20, "left": 20, "bottom": 20},
            width=800,
            height=300,
        ),
        rx.text("Population change for the four most populous US States"),
        justify="center",
        align="center"
    )


def examples() -> rx.Component:
    return rx.vstack(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Introduction", value="tab_intro", disabled=True),
                rx.tabs.trigger("Table", value="tab_table"),
                rx.tabs.trigger("Graph", value="tab_graph"),
                size="2",
            ),
            value=TabsState.value,
            on_change=lambda x: TabsState.change_value(x),
        ),

        rx.match(
            TabsState.value,
            ("tab_intro", intro()),
            ("tab_table", table()),
            ("tab_graph", graph()),
            rx.text("Please Select")
        ),
        align="center",
        justify="center"
    )
