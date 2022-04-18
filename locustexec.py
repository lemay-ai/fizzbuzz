from locust import HttpUser, task, between
from gevent.pool import Group
import random

tweets = ["i love dogs ",
          "i dont like cats",
          "i love golden retrievers",
          "that's my favourite restaurant",
          "I love my India!",
          "Donald Trump is so dumb"]

num_of_parallel_requests = 6


class AppUser(HttpUser):
    wait_time = between(0.05, 0.1)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def sentiment_page(self):
        group = Group()
        mytext = random.choice(tweets)
        for i in range(0, num_of_parallel_requests):
            group.spawn(self.client.get("/state_analysis/" + mytext))

        group.join()
