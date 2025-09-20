# ---- Build stage ----
FROM python:3.11-slim AS builder
WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install deps in venv
RUN python -m venv /venv \
    && /venv/bin/pip install --no-cache-dir --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

# ---- Runtime stage ----
FROM python:3.11-slim
WORKDIR /app

# Copy venv from builder
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy app code
COPY . .

# Run with Gunicorn (prod server)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:create_app()"]
