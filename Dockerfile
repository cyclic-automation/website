FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y curl \
    python3.9 \
    python3-pip \
    unzip && \
    curl -fsSL https://deb.nodesource.com/setup_18.0 | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /website
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN npm install

RUN reflex --version

STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]
