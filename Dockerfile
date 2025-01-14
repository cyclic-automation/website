FROM python:3.13

ENV PYTHONUNBUFFERED=1

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pnpm

WORKDIR /website
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN rm -rf node_modules
RUN npm install

# Handle SIGTERM signals correctly for Railway's container orchestration
STOPSIGNAL SIGTERM

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]