# FROM nginx
# COPY content /usr/share/nginx/html
# COPY conf /etc/nginx
# VOLUME /usr/share/nginx/html
# VOLUME /etc/nginx

# start by pulling the python image
FROM python:3.8-alpine
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app
RUN pip install --upgrade pip
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN pip install numpy==1.14.3
RUN pip install python-dateutil
RUN pip install --no-deps pandas==0.23.0
# copy every content from the local file to the image
COPY . /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["view.py" ]