FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app.py .

# Run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
