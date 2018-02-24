#!/bin/sh

cd /app
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --clear --no-input

exec gunicorn config.wsgi:application \
	    --name csv-webapp-server \
	    --bind 0.0.0.0:8000 \
	    --workers 3 \

exec "$@"
