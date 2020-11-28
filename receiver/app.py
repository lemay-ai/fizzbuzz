from flask import Flask, request
from time import time, sleep
import ast
import os
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)


@app.route('/', methods=['POST','GET'])
def hello(mongo=mongo):
	try:	
		incoming_dict=request.data
		incoming_dict=str(incoming_dict, 'utf-8')
		incoming_dict=ast.literal_eval(incoming_dict)
		received_time=time()*1000
		mydict={
			'number':incoming_dict['number'],
			'sent_time':incoming_dict['time'],
			'received_time':received_time,
			'latency':received_time-incoming_dict['time']} 
		mongo.db.numbers.insert_one(mydict)
	except:
		pass
	results=list(mongo.db.numbers.find())
	#result=mongo.db.numbers.find_one()
	print(results[-1])
	summed=0
	mylist=[]
	for entry in results[-10:]:
		summed+=entry['latency']
	mean_latency=summed/10
	#x = mycol.save(mydict)
	#query_results=posts.find().sort([("number", -1)]).limit(1)
	return """
<meta http-equiv="refresh" content="1" /> 
Hello World!<br>The highest number is {}. The average latency (for the last 10 requests) is {} """.format(results[-1]['number'],mean_latency)
#'latest number '+ str(results[-1]['number'])+'\n average latency (last 10 requests): ' + str(mean_latency)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
