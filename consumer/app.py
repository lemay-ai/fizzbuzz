from requests import post
from flask import Flask, request,jsonify,json,render_template
from redis import Redis
from rq import Queue,Worker
import time
import os
import ast
from flask_pymongo import PyMongo
import requests
#import myqueue
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/", methods=['GET','POST'])
def hello():

	try:

		producer.enqueue()
		receive_data=request.data.decode('UTF-8')
		print(receive_data)
		receive_data=ast.literal_eval(receive_data)
		received_time=time.time()
		mydata={
			'number':receive_data['number'],
			'time':receive_data['time'],
			'received_time':received_time,
			'latency':received_time-receive_data['time']
			}
		mongo.db.collection_requests.insert_one(mydata)
	except:
		pass
		
	receive_mongo = list(mongo.db.collection_requests.find())
	#print(receive_mongo)
	number = receive_mongo[-1]['number']
	#print(receive_mongo[-1])
	sum_latency = 0
	mean_latency = 0 
	
	for i in receive_mongo[-10:]:
		sum_latency+=i['latency']
	mean_latency=sum_latency/10
	return render_template('main.html', number=number, mean_latency=mean_latency)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)