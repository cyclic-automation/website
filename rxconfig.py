import reflex as rx

config = rx.Config(
    app_name="website",
    frontend_host="0.0.0.0",
    backend_host="0.0.0.0",
    frontend_port=10000,
    backend_port=10000,
    debug=False,
    dev_mode=False,
)
