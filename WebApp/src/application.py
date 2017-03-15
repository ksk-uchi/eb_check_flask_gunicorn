# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from app_config import BaseConfig, DevConfig
from app_logging import setup_logging
from views import top


app = Flask(__name__, template_folder='templates')
# 'APP_ENVIRONMENT' is defined by Dockerfile
app_env = os.getenv('APP_ENVIRONMENT', 'devel')

# Setting the application process configs
config = {
    'devel': 'app_config.DevConfig',
}
app.config.from_object(config[app_env])

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
db.init_app(app)

# logging Singleton object definition
setup_logging(env=app_env)
logger = logging.getLogger(__name__)

# Loading views
app.register_blueprint(top.app, url_prefix='/top')
logger.debug(app.config)

@app.errorhandler(500)
def handle_500_response(e):
    return 'Sorry'

if __name__ == '__main__':
    app.run()
