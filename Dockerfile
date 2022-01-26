FROM tiangolo/uwsgi-nginx:python3.6

ENV STATIC_URL /static
ENV STATIC_PATH /home/uavproject/Desktop/Docker-gpt2/app/static
WORKDIR /Docker-gpt2 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
expose 5000

