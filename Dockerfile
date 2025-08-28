# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=UTC \
    PORT=8000

WORKDIR /app

# Enable bytecode compilation and prefer copy mode for cache layers
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency file(s) and install deps
COPY pyproject.toml ./
RUN uv pip install --system -e .

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose the port for MCP communication
EXPOSE 8000

# Add health check to ensure the MCP server is ready
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health', timeout=5)" || exit 1

# Run the MCP server with HTTP transport for external access
CMD ["python", "main.py", "--http", "--port", "8000"]
