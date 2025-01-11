import reflex as rx

config = rx.Config(
    app_name="website",
    api_url="http://0.0.0.0",
    # backend_host="0.0.0.0",
    frontend_port=8000,
    backend_port=3000,
    debug=False,
    dev_mode=False,
)
