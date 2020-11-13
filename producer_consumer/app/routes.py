
from app import app, db
from app.models import Msg
from app.utils import *
import datetime
import json
from flask import render_template, request, jsonify, url_for, make_response
from sqlalchemy import func, desc



@app.route('/')
@app.route('/index')
def index():
    user = {'msg': 'dcshapiro!'}
    max_msg = db.session.query(func.max(Msg.msg_num)).scalar()
    avg_time = db.session.query(Msg).filter(Msg.timestamp >= datetime.datetime.now() - datetime.timedelta(seconds=10))\
        .with_entities(func.avg(Msg.time))\
        .scalar()

    return render_template('index.html', title='Home', user=user, max_msg = max_msg, avg_time = round(avg_time, 2))

@app.route('/calculate_result', methods = ["GET"])
def calculate_result():
    max_msg = db.session.query(func.max(Msg.msg_num)).scalar()
    avg_time = db.session.query(Msg).filter(Msg.timestamp >= datetime.datetime.now() - datetime.timedelta(seconds=10))\
        .with_entities(func.avg(Msg.time))\
        .scalar()
    res = jsonify({"msg_num" : "The max message #: {}".format(max_msg), "avg_time" : "The averga time of the calls for the last 10 seconds is {} milliseconds".format(round(avg_time, 2))})
    return res


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


