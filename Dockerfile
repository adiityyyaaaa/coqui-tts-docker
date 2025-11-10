FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git ffmpeg libsndfile1 espeak-ng curl \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (required for sudachipy)
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY src /app/src

CMD ["python", "src/demo.py"]
