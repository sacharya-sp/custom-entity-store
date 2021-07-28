#!/usr/bin/env bash

python manage.py collectstatic

gunicorn django_skeleton.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 &
nginx -g "daemon off;"
