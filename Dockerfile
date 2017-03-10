FROM       python:3.6.0

WORKDIR    /var/app

RUN        pip3 install virtualenv
RUN        virtualenv /var/app
RUN        /var/app/bin/pip install --cache-dir /src gunicorn

RUN        groupadd -g 2002 gunicorn
RUN        useradd -u 2002 -g gunicorn -M -s /bin/bash gunicorn
RUN        mkdir -p /usr/local/gunicorn/conf
RUN        mkdir -p /usr/local/gunicorn/log
RUN        chown -R gunicorn.gunicorn /usr/local/gunicorn

ADD . /var/app
RUN if [ -f /var/app/requirements.txt ]; then /var/app/bin/pip install -r /var/app/requirements.txt; fi

ENV        GUNICORN_NUM_WORKERS      4
ENV        GUNICORN_BIND             0.0.0.0:8080
ENV        GUNICORN_UID              gunicorn
ENV        GUNICORN_GID              gunicorn
ENV        GUNICORN_ACCESS_LOG       /usr/local/gunicorn/log/access.log
ENV        GUNICORN_ERROR_LOG        /usr/local/gunicorn/log/error.log

EXPOSE     8080

ADD        gunicorn-start.sh /

CMD        []
ENTRYPOINT ["/gunicorn-start.sh"]
