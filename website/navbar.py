import reflex as rx
from website.landing import landing

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.link(
                    rx.heading(
                        "Cyclic Automation", size="7", weight="bold", color_scheme="gray"
                    ),
                    href='/'
                )
            ),
            rx.hstack(
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
        ),
        bg=rx.color("sky", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )