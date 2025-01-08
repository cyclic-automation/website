import os
import reflex as rx

config = rx.Config(
    app_name="website",
    backend_host="0.0.0.0",  # Ensure it's accessible externally
    backend_port=int(os.environ.get("PORT", 8000)),  # Use Render's dynamic PORT
    frontend_port=1000,
    debug=False,
    dev_mode=False,
)
