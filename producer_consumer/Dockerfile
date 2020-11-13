FROM python:3.6-alpine

RUN adduser -D model

WORKDIR /home/producer_consumer

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY model.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP model.py

RUN chown -R model:model ./
USER model

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]