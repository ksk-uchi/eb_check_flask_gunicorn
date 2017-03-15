# -*- coding: utf-8 -*-

import datetime

class BaseConfig(object):
    DEBUG: False
    TESTING: False
    PROPAGATE_EXCEPTIONS: None
    PRESERVE_CONTEXT_ON_EXCEPTION: None
    SECRET_KEY: None
    PERMANENT_SESSION_LIFETIME: datetime.timedelta(31)
    USE_X_SENDFILE: False
    LOGGER_NAME: 'application'
    LOGGER_HANDLER_POLICY: 'always'
    SERVER_NAME: None
    APPLICATION_ROOT: None
    SESSION_COOKIE_NAME: 'session'
    SESSION_COOKIE_DOMAIN: None
    SESSION_COOKIE_PATH: None
    SESSION_COOKIE_HTTPONLY: True
    SESSION_COOKIE_SECURE: False
    SESSION_REFRESH_EACH_REQUEST: True
    MAX_CONTENT_LENGTH: None
    SEND_FILE_MAX_AGE_DEFAULT: datetime.timedelta(0,43200)
    TRAP_BAD_REQUEST_ERRORS: False
    TRAP_HTTP_EXCEPTIONS: False
    EXPLAIN_TEMPLATE_LOADING: False
    PREFERRED_URL_SCHEME: 'http'
    JSON_AS_ASCII: True
    JSON_SORT_KEYS: True
    JSONIFY_PRETTYPRINT_REGULAR: True
    JSONIFY_MIMETYPE: 'application/json'
    TEMPLATES_AUTO_RELOAD: None

class DevConfig(BaseConfig):
    # If DEBUG is True then ISE will be real ISE.
    # However if it is False then Flask can handle it on function which within app.errorhandling decorator.
    DEBUG = True