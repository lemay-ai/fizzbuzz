import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'




# FROM python:3.6-alpine

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




