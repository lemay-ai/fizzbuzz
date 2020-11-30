#!/usr/bin/env python3

"""POST server imports"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
"""postgres db"""
from postgrespy import DB
import time
from redis import Redis
from rq import Queue, Worker
import redisfunc 
import redisfunc 
import logging
log = logging.getLogger()
log.setLevel(logging.ERROR)

redis = Redis(host='redis')
q = Queue(name='fizzbuzzqueue', is_async=True, connection=redis)

def get_post_dict(string):
    param_list = string.split('&')
    # print(param_list)
    dic = {}
    for st in param_list:
        # print(st)
        if st.find('count=')!=-1:
            try:
                dic['count'] = int(st.split('=')[1])
            except:
                pass
        if st.find('timestamp=')!=-1:
            try:
                dic['timestamp'] = float(st.split('=')[1])
            except:
                pass
    if not dic:
        return None
    return dic

def consumer(data):
    print(data)

db = DB('consumed', hostname = 'db', port = '5432')

class RequestHandler(BaseHTTPRequestHandler):
    # def __init__(self):
    #     super(BaseHTTPRequestHandler)
    #     self.db = DB('consumed')
    def log_message(self, format, *args):
        return
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))
        # print(post_data.decode('utf-8'))
        t = time.time()
        self._set_response()
        resp = get_post_dict(post_data.decode('utf-8'))
        if resp:
            # print(resp)
            cmd = f"""
              INSERT INTO {db.tablename} (count, arrival_time, transmit_time)
              VALUES({resp['count']}, to_timestamp({t}), to_timestamp({resp['timestamp']}));
              """
            db.run_psql( cmd )
            myobj = {'count': resp['count'], 'arrival_time': t, 'transmit_time': resp['timestamp']}
            q.enqueue(redisfunc.push_post_request, myobj)

            # print(db.run_psql( 'SELECT * FROM consumed;'))
        # self._set_response()
        # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run_server(port=int(argv[1]))
    else:
        run_server()
