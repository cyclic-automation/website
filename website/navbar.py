import reflex as rx
from website.landing import landing


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(justify="start"),
            rx.hstack(
                rx.link(
                    rx.button("Home", variant="ghost"),
                    href="/"),
                rx.link(
                    rx.button("Client Portal", variant="ghost"),
                    href="login/"),
                rx.link(
                    rx.button("Examples", variant="ghost"),
                    href="/examples"),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.text("Contact"),
                            rx.icon("chevron-down"),
                            variant="ghost"
                        ),
                    ),
                    rx.menu.content(
                        rx.link("Email",
                                href="mailto:kyletarrao@cyclic-automation.io"),
                    ),
                ),
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
        ),
        padding="1em",
        # position="fixed",
        width="100%",
    )
