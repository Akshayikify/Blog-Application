# Multi-stage build for efficiency
FROM python:3.12-slim AS builder # Changed from 3.11-slim to 3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && mkdir -p /root/.local

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim # Changed from 3.11-slim to 3.12-slim
WORKDIR /app

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 8000

USER appuser
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
