FROM ubuntu:22.04

# Set noninteractive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    python3.9 \
    python3-pip \
    curl \
    unzip \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Node.js (required by Reflex for client-side builds)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install Reflex globally
RUN pip install reflex

# Ensure reflex command works in Docker
ENV PATH="/root/.local/bin:$PATH"

# Expose Reflex's default ports
EXPOSE 3000 8000

# Default command to run Reflex
CMD ["reflex", "run", "--env", "prod"]
