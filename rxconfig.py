import reflex as rx

config = rx.Config(
    app_name="website",
    frontend_host="0.0.0.0",
    # backend_host="0.0.0.0",
    frontend_port=3000,
    backend_port=8000,
    debug=False,
    dev_mode=False,
)
