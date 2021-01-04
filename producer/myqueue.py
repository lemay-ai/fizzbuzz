from redis import Redis
from rq import Queue,Worker
from time import sleep
import producer
import sys,os

initiating=True
while True:
    try:
        if initiating:
            queue = Queue( is_async = True, connection=Redis(host='redis', port=6379))
            job = queue.enqueue(producer.producer_posts)
            os.system("rq worker --url redis://redis:6379 &")
            print(job.id)
            initiating=False
            sleep(1)
        else:
            sleep(1)

    except:
        pass