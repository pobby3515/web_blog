# 1. Base image using Python 3.12-slim
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project source code
COPY . .

# 6. Expose default Cloud Run port (8080)
EXPOSE 8080

# 7. Start Gunicorn WSGI server tailored for Cloud Run
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} --workers 2 --threads 8 --timeout 0 app:app"]
