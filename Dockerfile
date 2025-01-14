# Use the official Python image as the base
FROM python:3.13

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"
RUN bun --version

WORKDIR /website
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN reflex export --no-zip

# Handle SIGTERM signals correctly for Railway's container orchestration
STOPSIGNAL SIGTERM

# Expose the necessary ports
EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]