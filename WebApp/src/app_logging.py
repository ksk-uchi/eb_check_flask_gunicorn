# -*- coding: utf-8 -*-
import os
import json
import logging.config

def setup_logging(env):
    path_dict = {
        'devel': 'logging_confs/devel.json'
    }
    path = path_dict[env]
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
