"""Flask config."""
  
import json
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)


class Config(object):

    def __init__(self):
        self._read_config()

    def _read_config(self):
        f = open('config.json', 'r')
        config = json.load(f)
        for key, value in config.items():
            setattr(self, key, value)