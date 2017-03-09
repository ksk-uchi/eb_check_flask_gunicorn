#!/bin/bash

cd /var/app

. bin/activate

WSGI_MODULE=application:app


gunicorn --chdir /var/app/src -b $GUNICORN_BIND -w $GUNICORN_NUM_WORKERS --reload --access-logfile $GUNICORN_ACCESS_LOG_FILE \
    --error-logfile $GUNICORN_ERROR_LOG_FILE $WSGI_MODULE

