import reflex as rx


class LoginState(rx.State):
    login_data: dict = {}

    def handle_login(self, login_data: dict):
        self.login_data = login_data


def login() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.heading(
                    "Login",
                    size="6",
                    width="100%",
                    align="center",
                ),
                rx.input(
                    name='email',
                    placeholder="email",
                    # type="email",
                    required=True,
                    size="3",
                    width="100%",
                ),
                rx.input(
                    name='password',
                    placeholder="password",
                    # type="password",
                    required=True,
                    size="3",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%", type="submit"),
                spacing="6",
                width="100%",
                align="center"
            ),
            on_submit=rx.toast.error("Login Failed", position="top-center"),
            reset_on_submit=True
        ),
        size="4",
        max_width="28em",
        width="100%",
    )

