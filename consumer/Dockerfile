FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN touch /code/__init__.py
COPY redisfunc.py /code/
COPY postgrespy.py /code/
RUN pip install -r requirements.txt
