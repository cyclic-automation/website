import os
import reflex as rx

config = rx.Config(
    app_name="website",
    backend_host="0.0.0.0",  # Ensure it's accessible externally
    frontend_port=10000,
    backend_port=10000,
    debug=False,
    dev_mode=False,
)
