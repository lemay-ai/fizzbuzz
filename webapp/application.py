"""
Demo Flask application to test the operation of Flask with socket.io

Aim is to create a webpage that is constantly updated with random numbers from a background python process.

30th May 2014

===================

Updated 13th April 2018

+ Upgraded code to Python 3
+ Used Python3 SocketIO implementation
+ Updated CDN Javascript and CSS sources

"""

# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
__author__ = 'slynn'

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=False, engineio_logger=False)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

from pandas import DataFrame
# import psycopg2
# conn = psycopg2.connect("user='postgres' host='db' password='postgres'")

def get_psql_data(conn):
    cur = conn.cursor()
    cmd =   """
            SELECT * 
            FROM consumed 
            ORDER BY arrival_time DESC 
            LIMIT 10;
            """
    cur.execute(cmd)
    time_df = DataFrame(cur.fetchall(), columns=['arrival_time', 'transmit_time', 'count'])
    time = str(time_df[['transmit_time', 'arrival_time']].diff(axis=1, periods=1)['arrival_time'].mean())
    cmd =   """
            SELECT * 
            FROM consumed 
            ORDER BY count DESC 
            LIMIT 10;
            """
    cur.execute(cmd)
    max_df = DataFrame(cur.fetchall(), columns=['arrival_time', 'transmit_time', 'count'])
    
    return max_df.max()[2], time

def randomNumberGenerator():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    #infinite loop of magical random numbers
    import psycopg2
    conn = psycopg2.connect("user='postgres' host='db' password='postgres'")

    print("Making random numbers")
    while not thread_stop_event.isSet():
        count, time_diff = get_psql_data(conn)
        number = round(random()*10, 3)
        # print(number)
        socketio.emit('newnumber', {'number': int(count)}, namespace='/test')
        socketio.emit('newnumber2', {'number': str(float(time_diff.split('.')[-1][0:5])/100.0)+'ms ('+time_diff+')'}, namespace='/test')
        # socketio.emit('newnumber2', {'number': time_diff}, namespace='/test')
        socketio.sleep(1)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(randomNumberGenerator)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
