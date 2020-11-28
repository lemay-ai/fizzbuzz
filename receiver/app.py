from flask import Flask, request
from time import time, sleep
import ast

import pymongo

myclient = pymongo.MongoClient("mongodb://10.5.0.3:27017/mydatabase")
mydb = myclient["mydatabase"]
mycol = mydb["messages"]

app = Flask(__name__)
@app.route('/', methods=['POST'])
def hello(mycol=mycol):
    incoming_dict=request.data
    incoming_dict=str(incoming_dict, 'utf-8')
    incoming_dict=ast.literal_eval(incoming_dict)
    received_time=time()*1000
    
    mydict={'number':incoming_dict['number'],
	'sent_time':incoming_dict['time'],
	'received_time':str(received_time),
	'latency':str(received_time-float(incoming_dict['time']))
	} 
    x = mycol.insert_one(mydict)

    return 'number '+ str(incoming_dict['number']) +'sent_time' + str(incoming_dict['time']) + 'received_time' + str(received_time) + 'latency' + str(received_time-float(incoming_dict['time']))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
