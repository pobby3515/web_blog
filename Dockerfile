# 1. Base image using Python 3.12-slim
FROM python:3.13

# 2. Install uv from official Astral binary image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# 4. Set working directory
WORKDIR /app

# 5. Install dependencies into virtual environment via uv sync
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-cache

# 6. Copy application source code
COPY . .

# 7. Place virtualenv into PATH
ENV PATH="/app/.venv/bin:$PATH"

# 8. Expose default port (8080)
EXPOSE 8080

# 9. Start app using uv run
CMD ["sh", "-c", "uv run python app.py"]
