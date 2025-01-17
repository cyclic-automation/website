FROM python:3.13

ARG PORT=10000

#ARG API_URL
#ENV PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT} PYTHONUNBUFFERED=1

RUN apt-get update -y && apt-get install -y caddy npm && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y npm
npm install --silent

WORKDIR /app
COPY . .

RUN pip install --root-user-action=ignore -r requirements.txt

RUN reflex init

RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web

STOPSIGNAL SIGKILL

EXPOSE $PORT

CMD caddy start && exec reflex run --env prod --backend-only