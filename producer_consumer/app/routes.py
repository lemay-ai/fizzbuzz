
from app import app, db
from app.models import Msg
from app.utils import *
import datetime
import json
from flask import render_template, request, jsonify, url_for, make_response
from sqlalchemy import func, desc
from redis import Redis
from rq import Queue

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    user = {'msg': 'dcshapiro!'}
    max_msg, avg_time = data_get()
    if max_msg and avg_time:
        return render_template('index.html', title='Home', user=user, max_msg = max_msg, avg_time = round(avg_time, 2))
    else:
        return render_template('index.html', title='Home', user=user, max_msg = max_msg, avg_time = avg_time)


##Route for updating the msg # and avg time of the last call within past 10 seconds
@app.route('/calculate_result', methods = ["GET", "POST"])
def calculate_result():
    max_msg, avg_time = data_get()
    if avg_time:
        res = jsonify({
            "msg_num" : "The max message #: {}".format(max_msg), 
            "avg_time" : "The averga time of the calls for the last 10 seconds is {} milliseconds".format(round(avg_time, 2))
            })
        return res
    else:
        return ("Something went wrong", 500)


## The consumer routes
@app.route('/consumer', methods=["POST"])
def consumer():
    arrival_time = datetime.datetime.now()
    if request.method == "POST":
        job = app.task_queue.enqueue(db_insert, request.data, arrival_time)
        res = {"message" : f"The request was completed, job id: {job.id}"}
        return jsonify(res)
    else:
        return "The request method has to be POST"


