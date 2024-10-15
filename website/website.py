import reflex as rx
from website.base import base
from website.landing import landing
from website.login import login

class State(rx.State):
    """The app state."""

    ...


def index(content: rx.Component) -> rx.Component:
    return rx.fragment(
        # rx.theme_panel(),
        base(content)
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        scaling="100%",
        has_background=True,
        radius="small",
        gray_color="sand",
        accent_color="bronze"
    )
)

app.add_page(
    index(landing()),
    route="/",
    title="Cyclic Automation")

app.add_page(
    index(login()),
    route="/login",
    title="Login",
)

