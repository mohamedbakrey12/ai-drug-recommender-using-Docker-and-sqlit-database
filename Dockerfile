# صورة أساس خفيفة
FROM python:3.9-slim

# مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات
COPY . .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# فتح المنفذ
EXPOSE 8501

# تشغيل التطبيق
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
