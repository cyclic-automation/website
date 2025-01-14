import os
import reflex as rx

config = rx.Config(
    app_name="website",
    deploy_url="https://website-epp6.onrender.com",
    backend_host="0.0.0.0",
    backend_port=int(os.environ.get("PORT", 10000)),
    debug=False,
    dev_mode=False,
)
