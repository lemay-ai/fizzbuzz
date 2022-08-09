#!/bin/sh
gunicorn wsgi:app -w 2 --threads 8 -b 0.0.0.0:5000 