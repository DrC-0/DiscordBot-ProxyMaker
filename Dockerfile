FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install system dependencies for OpenCV and other libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (frozen to ensure exact versions)
RUN uv sync --frozen --no-cache

# Copy project files
COPY . .

# Run the bot by default
CMD ["uv", "run", "pdfbot.py"]
