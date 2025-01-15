FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    python3.9 \
    python3-pip

WORKDIR /website
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN reflex --version

STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]
