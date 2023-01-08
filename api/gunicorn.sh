#!/bin/sh
exec gunicorn wsgi:app -w 1 --threads 1 --log-level debug -b 0.0.0.0:5000