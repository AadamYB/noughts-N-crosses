FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-tk libglib2.0-0 libx11-6 && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY tests ./tests

CMD ["python3", "app/main.py"]
