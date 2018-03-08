import os
import logging

class Config(object):
    DEBUG = True
    LOGGER_HANDLER_POLICY = logging.INFO
    SECRET_KEY = os.environ.get('FLASK_BOILERPLATE_SECRET_KEY')
