FROM python:3.12-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y unzip

# Set up your environment
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["reflex", "run", "--env", "prod"]
