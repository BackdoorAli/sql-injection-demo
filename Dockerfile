# === Base Stage: Builder ===
FROM python:3.10-slim AS builder

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# === Final Stage: Runtime ===
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app /app

# Environment variable to choose app type
ENV APP_MODE=insecure

# Expose Flask default port
EXPOSE 5000

# Entrypoint logic based on APP_MODE
CMD ["sh", "-c", "if [ \"$APP_MODE\" = \"secure\" ]; then python run_secure.py; else python run_insecure.py; fi"]