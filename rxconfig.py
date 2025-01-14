import reflex as rx

config = rx.Config(
    app_name="website",
    deploy_url="https://website-epp6.onrender.com",
    backend_host="0.0.0.0",
    frontend_port=10000,
    backend_port=8000,
    debug=False,
    dev_mode=False,
)
