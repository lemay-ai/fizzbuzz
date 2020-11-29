from time import time, sleep
from requests import post
number=0
while True:
  for i in range(0,10):
    data={'number':number, 'time':time()*1000}
    data=str(data)
    post('http://10.5.0.4:5000',data = data) #this is the step to post from this (producer) container to myqueuer/receiver container
    number+=1
    sleep(0.01)
  sleep(0.9)

