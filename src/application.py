# -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from views import top

app = Flask(__name__)

app.register_blueprint(top.app)

if __name__ == '__main__':
    app.logger.config.fileConfig('log_config.yml', defaults='file')
    app.run()
