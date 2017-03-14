# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask

from app_config import BaseConfig, DevConfig
from app_logging import setup_logging
from views import top


app = Flask(__name__)
# 'APP_ENVIRONMENT' is defined by Dockerfile
app_env = os.getenv('APP_ENVIRONMENT', 'devel')

# Setting the application process configs
config = {
    'devel': 'app_config.DevConfig',
}
app.config.from_object(config[app_env])

# logging Singleton object definition
setup_logging(env=app_env)
logger = logging.getLogger(__name__)

# Loading views
app.register_blueprint(top.app, url_prefix='/top')


@app.errorhandler(500)
def handle_500_response(e):
    return 'Sorry'

if __name__ == '__main__':
    app.run()
