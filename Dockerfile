# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.11

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /website
COPY . .

# Install app requirements and reflex in the container
RUN pip install -r requirements.txt

RUN npm run build

# Deploy templates and prepare app
RUN reflex init

EXPOSE 3000 8000

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD reflex run --env prod