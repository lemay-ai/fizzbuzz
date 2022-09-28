#!/bin/bash
exec gunicorn --config gunicorn_config.py app:flask_app
# exec python app.py