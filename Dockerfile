FROM jupyter/scipy-notebook
FROM python:3.10

RUN pip install transformers
COPY ./requirements.txt ./requirements.txt

COPY ./model/model.pkl ./model/model.pkl


RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app.py ./app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
