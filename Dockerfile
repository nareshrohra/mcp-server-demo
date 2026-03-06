FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "app.py"]
