FROM python:3.6-alpine

RUN adduser -D model

WORKDIR /home/model

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY templates templates
COPY migrations migrations
COPY model.py config.py boot.sh ./
RUN chmod +x boot.sh


RUN chown -R model:model ./
USER model

ENTRYPOINT ["./boot.sh"]




# FROM python:3.8.6-alpine

# WORKDIR /home/model

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY app app
# COPY templates templates
# COPY model.py config.py boot.sh ./
# RUN chmod +x boot.sh

# ENV FLASK_APP model.py
# ENV FLASK_ENV development

# EXPOSE 5000

# ENTRYPOINT ["./boot.sh"]