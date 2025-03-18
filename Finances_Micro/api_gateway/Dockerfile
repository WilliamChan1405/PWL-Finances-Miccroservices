# Gunakan base image Python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements dan install dependensi
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY api_gateway.py api_gateway.py

# Jalankan aplikasi saat container dimulai
CMD ["python", "api_gateway.py"]
