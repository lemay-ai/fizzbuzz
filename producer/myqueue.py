from redis import Redis
from rq import Queue,Worker
import producer

queue = Queue( is_async = True, connection=Redis(host='127.0.0.1', port=6379))


job = queue.enqueue(producer.producer_posts)
print(job.id) 