FROM       python:3.6.0

WORKDIR    /var/app

RUN        pip3 install --cache-dir /src gunicorn

RUN        groupadd -g 2002 gunicorn
RUN        useradd -u 2002 -g gunicorn -M -s /bin/bash gunicorn
RUN        mkdir -p /var/log/app/
RUN        chown -R gunicorn.gunicorn /var/log/app

ADD . /var/app
RUN if [ -f /var/app/requirements.txt ]; then pip3 install -r /var/app/requirements.txt; fi

ENV        GUNICORN_NUM_WORKERS      1
# timeout is 2 minutes
ENV        GUNICORN_WORDER_TIMEOUT   120
ENV        GUNICORN_BIND             0.0.0.0:8080
ENV        GUNICORN_UID              gunicorn
ENV        GUNICORN_GID              gunicorn
ENV        GUNICORN_ACCESS_LOG       /var/log/app/gunicorn_access.log
ENV        GUNICORN_ERROR_LOG        /var/log/app/gunicorn_error.log
ENV        WSGI_MODULE               application:app

# Defined only an application environment level since it is the root information to handle all application environment variables.
# See `./src/application.py` all application environment variables are defined at there except an application environment level.
ENV        APP_ENVIRONMENT           devel

EXPOSE     8080

CMD        gunicorn --chdir /var/app/src \
                    -b $GUNICORN_BIND \
                    -w $GUNICORN_NUM_WORKERS \
                    -t $GUNICORN_WORDER_TIMEOUT \
                    -u $GUNICORN_UID \
                    -g $GUNICORN_GID \
                    # --access-logfile $GUNICORN_ACCESS_LOG \
                    # --error-logfile $GUNICORN_ERROR_LOG \
                    --reload $WSGI_MODULE
