FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash \
    && mv /root/.bun/bin/bun /usr/local/bin/

# Add Bun to PATH
ENV PATH="/usr/local/bin:$PATH"

# Set working directory
WORKDIR /website
COPY . /website

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to start the Reflex application
CMD ["reflex", "run", "--env", "prod"]
