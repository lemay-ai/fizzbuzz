from time import time, sleep
from requests import post


def producer_posts():
  message_number=0
  while True:
    for i in range(0,10):
      data={'number':message_number, 'time':time()}
      #data=str(data)
      r=post('http://consumer:5000',json = data) 
      #print(r)#this is the step to post from this (producer) container to myqueuer/receiver container
      message_number+=1
      sleep(0.01)
    sleep(0.9)


   