FROM ubuntu:20.04

RUN apt-get install -y  \
    python3 \
    python3-pip

WORKDIR /website
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]