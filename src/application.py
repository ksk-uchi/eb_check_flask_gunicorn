# -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from app_config import BaseConfig, DevConfig
from views import top


def _get_config_obj():
    env = os.environ.get('APP_ENVIRONMENT', 'prod')
    if env == 'devel':
        return DevConfig
    else:
        return BaseConfig

app = Flask(__name__)
conf = _get_config_obj()
app.config.from_object(conf)
app.register_blueprint(top.app)

if __name__ == '__main__':
    app.run()
