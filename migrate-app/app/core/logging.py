import logging

def config_logger():
    logging.basicConfig(filename='app-errors.log', level=logging.WARNING)