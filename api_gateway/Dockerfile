FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Dodaj to ⬇⬇⬇
RUN pip install --no-cache-dir pytest

COPY . .

CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8000"]
