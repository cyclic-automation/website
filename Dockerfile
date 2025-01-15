FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&  \
    apt-get install -y \
    python3 \
    python3-pip \
    curl \
    unzip \
    nodejs \
    npm \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /website
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]