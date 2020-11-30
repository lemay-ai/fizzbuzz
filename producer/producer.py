import requests
import time
from time import sleep
from redis import Redis
from rq import Queue, Worker
import redisfunc 

url = 'http://consumer:8001'
i = 0

def push_post_request(url, data):
    resp = requests.post(url, data)
    return resp

# q = Queue(connection=Redis(host='producer', port=6379, decode_responses=True))
# q = Queue(is_async=False, connection=Redis(host='redis'))
redis = Redis(host='redis')
q = Queue(name='fizzbuzzqueue', is_async=True, connection=redis)


while True:
	myobj = {'count': i, 'timestamp': time.time()}
	x = requests.post(url, data = myobj)
	q.enqueue(redisfunc.push_post_request, myobj)
	# print(i, time.time())
	i += 1
	sleep(0.1)

