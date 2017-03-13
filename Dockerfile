FROM       python:3.6.0

WORKDIR    /var/app

RUN        pip3 install --cache-dir /src gunicorn

RUN        groupadd -g 2002 gunicorn
RUN        useradd -u 2002 -g gunicorn -M -s /bin/bash gunicorn
RUN        mkdir -p /usr/local/gunicorn/conf
RUN        mkdir -p /usr/local/gunicorn/log
RUN        chown -R gunicorn.gunicorn /usr/local/gunicorn

ADD . /var/app
RUN if [ -f /var/app/requirements.txt ]; then pip3 install -r /var/app/requirements.txt; fi

ENV        GUNICORN_NUM_WORKERS      4
ENV        GUNICORN_BIND             0.0.0.0:8080
ENV        GUNICORN_UID              gunicorn
ENV        GUNICORN_GID              gunicorn
ENV        GUNICORN_ACCESS_LOG       /usr/local/gunicorn/log/access.log
ENV        GUNICORN_ERROR_LOG        /usr/local/gunicorn/log/error.log
ENV        WSGI_MODULE               application:app

EXPOSE     8080

ADD        gunicorn-start.sh /

CMD        gunicorn --chdir /var/app/src -b $GUNICORN_BIND -w $GUNICORN_NUM_WORKERS --reload --access-logfile $GUNICORN_ACCESS_LOG \
                    --error-logfile $GUNICORN_ERROR_LOG $WSGI_MODULE
