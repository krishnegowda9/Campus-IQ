FROM python:3.11-slim

WORKDIR /app

# Ensure model weights are cached inside the container
ENV HF_HOME=/app/hf_cache

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Receive the HF token to authenticate during build
ARG HF_TOKEN
ENV HF_TOKEN=${HF_TOKEN}

# Pre-download models into the image during docker build
RUN python -c "import rag_pipeline; print('Models pre-downloaded successfully!')"

EXPOSE 7860

CMD ["python", "app.py"]