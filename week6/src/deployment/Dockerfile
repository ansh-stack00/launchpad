FROM python:3.11-slim

WORKDIR /app

COPY src /app/src
COPY src/deployment/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.deployment.api:app", "--host", "0.0.0.0", "--port", "8000"]
