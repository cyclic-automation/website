FROM python:3.11

RUN apt-get update -y && apt-get install -y caddy && rm -rf /var/lib/apt/lists/*

WORKDIR /website
COPY . .

RUN pip install -r requirements.txt

RUN reflex init

RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web

EXPOSE 3000 8000

STOPSIGNAL SIGKILL

CMD reflex run --env prod --backend-only