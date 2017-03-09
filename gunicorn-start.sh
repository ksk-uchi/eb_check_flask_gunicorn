#!/bin/bash

cd /var/app

. bin/activate

WSGI_MODULE=application:app

gunicorn --chdir /var/app/src -b $GUNICORN_BIND -w $GUNICORN_NUM_WORKERS --reload $WSGI_MODULE

