# fizzbuzz

This repo demonstrates the consumer-producer behavior with POST requests. A dashboard and jupyter notebook is made available for introspection. Further redis queue that enques responses from producer and consumer. Repo was tested on ubuntu 18.04 and Docker version 19.03.1

#### How to run

clone the repo by
```
git clone git@github.com:ratmcu/fizzbuzz.git
```

might need to switch to the master by

```
git pull origin master
```

then run docker-compose, docker-compose can be installed via [Install Docker Compose](https://docs.docker.com/compose/install/)

```
cd fizzbuzz
docker-compose up
```

everything should be up consumer, producer, redis, postgress db, web app and the notebook.

#### Introspections

To visit the note book use the url printed at the end. url should be visible in the following format

```
http://127.0.0.1:8888/?token=b6cea60db05fb9911007ccf892731488a471fa629cf528cd
```
notebook to query the system's psql database can be found inside "work" directory 

web app that updates the system statistics can be reached via [http://localhost:5000/](http://localhost:5000/)

redis queue can be executed with the following command

```
rq worker -u redis://localhost:6379 fizzbuzzqueue --burst
```

