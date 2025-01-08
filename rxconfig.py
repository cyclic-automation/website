import reflex as rx

config = rx.Config(
    app_name="website",
    env="prod",
    frontend_port=10000,
    backend_host="0.0.0.0"
)
