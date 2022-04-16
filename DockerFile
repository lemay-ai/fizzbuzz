# syntax=docker/dockerfile:1
FROM python:3.7
COPY . /app
EXPOSE 8080
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "api.py"]