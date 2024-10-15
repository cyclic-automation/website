import reflex as rx
from website.landing import landing

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                spacing="5",
            ),
            rx.hstack(
                rx.link(
                    rx.button("Home", variant="ghost"),
                    href="/"),
                rx.link(
                    rx.button("Client Portal", variant="ghost"),
                    href="login/"),
                rx.link(
                    rx.button("Contact", variant="ghost"),
                    href="mailto:kyletarrao@cyclic-automation.io"),
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
        ),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )