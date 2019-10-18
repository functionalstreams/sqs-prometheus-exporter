FROM python:3.7-alpine3.9

COPY src/main.py /app/
COPY requirements.txt VERSION /tmp/

WORKDIR /tmp
RUN pip3 install -r requirements.txt && rm -rf /tmp/*

WORKDIR /app

CMD ["python3", "/app/main.py"]
