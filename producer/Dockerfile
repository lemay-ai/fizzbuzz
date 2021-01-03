FROM python:3
COPY . /app
WORKDIR /app
COPY producer.py /app
RUN pip install -r requirements.txt
CMD python ./myqueue.py