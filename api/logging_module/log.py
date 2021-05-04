""" math_master DOCSTRING 1.0"""
import logging
from pythonjsonlogger import jsonlogger


class Log:
    """ math_master DOCSTRING 1.0"""
    logger = None
    formatter = None
    def __init__(self, app):
        """ math_master DOCSTRING 1.0"""
        app.logger.disabled = True
        log = logging.getLogger('werkzeug')
        log.disabled = True

    def get_logger(self):
        """ math_master DOCSTRING 1.0"""
        self.logger = logging.getLogger("math_master")
        log_handler = logging.StreamHandler()
        formatter = self.set_json_formatter(fmt='%(levelname) %(name) \
                                                %(filename) %(module) %(funcName) %(lineno) '
                                                '%(message) %(asctime)',
                                                datefmt='%m/%d/%Y %I:%M:%S %p')
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        return self.logger

    def set_json_formatter(self, fmt, datefmt):
        """ math_master DOCSTRING 1.0"""
        self.formatter = jsonlogger.JsonFormatter(fmt, datefmt)
        return self.formatter
