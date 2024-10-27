#!/bin/sh

python manage.py migrate

# Start the Django server in the background
python manage.py runserver 0.0.0.0:8000 &

# Run other management command (if this is shorter-running)
python manage.py fetch_transfer_events

# Run long-running management command in the background
python manage.py fetch_live_transfer_events &

# Wait indefinitely to keep the container running
wait
