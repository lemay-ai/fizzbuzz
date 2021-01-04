#!/bin/sh
rq worker --url redis://redis:6379
python3 myqueue.py 