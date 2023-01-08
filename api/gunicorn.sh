#!/usr/bin/env bash
exec gunicorn wsgi:app -w 2 --threads 2 --log-level debug -b 0.0.0.0:5000