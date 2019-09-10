import constants
import logging

import yaml

CONF = None
def load_conf(conf_file=constants.CONF_FILE):
    global CONF
    if CONF is None:
        with open(conf_file) as cf:
            CONF = yaml.load(cf)
            return CONF
    else:
        return CONF


def logger(log_file=constants.LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'):
    logging.basicConfig(filename=log_file, level=level, format=format)
    return logging


