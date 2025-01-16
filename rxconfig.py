import os
import reflex as rx

config = rx.Config(
    app_name="website",
    api_url="https://website-mflc.onrender.com",
    frontend_port=3000,
    backend_port=8000,
    debug=False,
    dev_mode=False,
)
