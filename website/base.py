import reflex as rx
from website.navbar import navbar

def base(content: rx.Component) -> rx.Component:
    return rx.vstack(
        navbar(),

        content,

        rx.spacer(),
        rx.text("Cyclic Automation", weight="light"),

        align="center"
    )