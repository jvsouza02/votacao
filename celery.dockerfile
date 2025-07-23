FROM python:3.13.5-slim

WORKDIR /votacao

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]
