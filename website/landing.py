import reflex as rx
from rxconfig import config


def landing() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.vstack(
                rx.spacer(),
                rx.image(
                    src="/logo.png",
                    border_radius="25%",
                    height=rx.breakpoints(
                        initial="50vh",
                        sm="55vh",
                        lg="55vh"
                    )
                ),
                rx.heading("Custom Automated Systems To Scale Your Business",
                           size=rx.breakpoints(
                               initial="7",
                               sm="8",
                               lg="9"
                           ),
                           align="center"
                           ),
                align="center",
                justify="center"
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),

            rx.heading("Services Include:", size="6"),
            rx.list.unordered(
                rx.list.item(
                    rx.text.strong("Data Processing, Formatting, Cleansing"),
                    " of files, PDFs, spreadsheets, CSVs, etc"),
                rx.list.item(
                    rx.text.strong("Data Scraping"),
                    " from scanned documents, emails or webportals"),
                rx.list.item(
                    rx.text.strong("Data Analytics and Visualization")),
                rx.list.item(
                    rx.text.strong("Database Management and Data Entry")),
                rx.list.item(
                    rx.text.strong("Perform Calculations")),
                rx.list.item(
                    rx.text.strong("Notifications"),
                    " including sending/receiving emails, texts"),
                rx.list.item(
                    rx.text.strong("Event Monitoring"),
                    " websites, queues, emails"),
                rx.list.item(
                    rx.text.strong("Application Integration"),
                    " with apps like Excel, Quickbooks, CRMs, Slack, FTP"),
                rx.list.item(
                    rx.text.strong("Encryption")),
                rx.list.item(
                    "Automated ",
                    rx.text.strong("Market Research")),
                rx.list.item(
                    rx.text.strong("Interact With Clients"),
                    " through updates, reminders and forms"),
            ),
            rx.text("Pricing is calculated as a fraction of the labor that it replaces."),

            rx.divider(),

            rx.heading("Prior Projects:", size="6"),
            rx.list.unordered(
                rx.list.item(
                    rx.text.strong("Client Onboarding Automation"),
                    " managing form queue (Jotform) for new clients and preparing them in file system (Google Drive),"
                    " CRM (CLIO), and sending internal summary email."),
            ),
            rx.list.unordered(
                rx.list.item(
                    rx.text.strong("Court Case Record Scraper"),
                    " collecting pdf records from the New York State Courts Electronic Filing (NYSCEF) system,"
                    " then extracting the data as entries in a spreadsheet overview."),
            ),

            rx.divider(),

            rx.heading("Founded And Operated By:", size="6"),
            rx.image(
                src="/portrait.jpeg",
                width="20%",
                height="30%",
                border_radius="25%",
            ),
            rx.heading("Kyle Tarrao", size="6"),
            rx.list.unordered(
                rx.list.item(
                    rx.text.strong("Automation Engineer"),
                    " - Billtrust"),
                rx.list.item(
                    rx.text.strong("Software Engineer"),
                    " - Northrop Grumman"),
                rx.list.item(
                    rx.text.strong("Bachelor of Electrical Engineering"),
                    " - Grove School, CUNY City College of New York"),
            ),

            spacing="5",
            align="center",
            min_height="85vh",
        ),
    )
