
from app import app, db
from app.models import Msg
from app.utils import *
import datetime
import json
from flask import render_template, request, redirect, url_for, make_response, jsonify
from sqlalchemy import func, desc
import time





@app.route('/')
@app.route('/index')
def index():
    user = {'msg': 'dcshapiro!'}
    max_msg = db.session.query(func.max(Msg.msg_num)).scalar()
    avg_time = db.session.query(Msg).filter(Msg.timestamp >= datetime.datetime.now() - datetime.timedelta(seconds=10))\
        .with_entities(func.avg(Msg.time))\
        .scalar()
    print(avg_time)
    return render_template('index.html', title='Home', user=user, max_msg = max_msg, avg_time = round(avg_time, 2))


## The consumer routess
@app.route('/consumer', methods=["POST"])
def consumer():
    arrival_time = datetime.datetime.now()
    if request.method == "POST":
        job = app.task_queue.enqueue(db_insert, request.data, arrival_time)
        res = {"message" : f"The request was completed, job number {job.id}"}
        return jsonify(res)
    else:
        return "The request method has to be POST"

# ##The producer routes
# @app.route('/producer', methods = ["GET", "POST"])
# def producer():
#     url = "http://localhost:5000/consumer"
#     headers = {'content-type': 'application/json'}
#     for i in range(0, 100):
#         start = datetime.datetime.now()
#         data = { "msg_num": i, "start" : start}
#         reqs.post(url, data=json.dumps(data, default = myconverter), headers=headers)
#     return redirect(url_for("index"))

