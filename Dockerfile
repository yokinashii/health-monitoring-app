FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "api_gateway.api_gateway:app", "--host", "0.0.0.0", "--port", "8000"]
