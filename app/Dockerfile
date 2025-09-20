# ---------- Stage 1: Build ----------
FROM python:3.11-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Upgrade pip + setuptools to patched versions, then install deps
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools==78.1.1 wheel \
 && pip install --user --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Bring in the built dependencies
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:${PATH}"

# Copy app source
COPY . .

# Run as non-root for security
RUN useradd -r -u 10001 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080
# lightweight healthcheck (optional; keeps hadolint happy too)
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz')" || exit 1

CMD ["python", "app.py"]
