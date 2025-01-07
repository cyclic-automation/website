import reflex as rx
from website.base import base
from website.landing import landing
from website.login import login
from website.examples import examples

analytics_script = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4SP16XF9TW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4SP16XF9TW');
</script>
"""

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
        accent_color="indigo"
    )
)

app.head_components.append(rx.html(analytics_script))

app.add_page(
    index(landing()),
    route="/",
    title="Cyclic Automation")

app.add_page(
    index(login()),
    route="/login",
    title="Login",
)

app.add_page(
    index(examples()),
    route="/examples",
    title="Examples",
)

if __name__ == "__main__":
    rx.run()
