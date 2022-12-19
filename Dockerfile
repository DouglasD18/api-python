FROM python:3.10-slim-buster

COPY . /app

RUN pip install fastapi==0.88.0 && pip install uvicorn==0.20.0

WORKDIR /app

CMD ["uvicorn", "api.main:app", "--port=8080"]