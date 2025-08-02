FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
WORKDIR /app/astro-backend/astro-backend

CMD ["python", "-m", "uvicorn", "astro_backend_main:app", "--host", "0.0.0.0", "--port", "8000"] 