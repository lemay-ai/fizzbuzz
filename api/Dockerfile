FROM python:3.8.0

ADD . .
#ADD /api/v1/inference ./api/v1/inference
#COPY ./api/v1/api_server.py ./api/v1/api_server.py
#COPY ./api/v1/requirments.txt ./api/v1/requirments.txt

WORKDIR /api

RUN python -m pip install pip==21.0.1
RUN pip install -r requirements.txt

#WORKDIR ..

EXPOSE 5000
RUN chmod -R 777 ./gunicorn.sh

ENTRYPOINT ["sh", "gunicorn.sh"]

