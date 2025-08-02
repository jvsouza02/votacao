FROM python:3.13.5-slim

WORKDIR /votacao

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 50051

CMD ["python", "grpc_server.py", "--host", "0.0.0.0", "--port", "50051"]

