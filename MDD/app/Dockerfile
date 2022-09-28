FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip install --upgrade pip

ADD . /app

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
