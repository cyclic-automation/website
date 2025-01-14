FROM python:3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /website
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Handle SIGTERM signals correctly for Railway's container orchestration
STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]