FROM python:3.12-slim

WORKDIR /app
COPY check_leak.py .

RUN pip install requests

ENTRYPOINT ["python", "check_leak.py"]
