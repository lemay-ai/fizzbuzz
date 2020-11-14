#!/bin/sh
while true; do
    source venv/bin/activate
    flask db init
    flask db migrate -m "intialize db"
    flask db upgrade
    flask run --host=0.0.0.0
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
