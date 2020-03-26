import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
#from json import loads, JSONDecodeError
from pathlib import Path

class Config(defaultdict, ABC):
    @abstractmethod
    def __init__(self):
        self['mode'] = 'BASE'
        #self['flask'] = {}
        self["port"] = 6291 #check port
        #self['database'] = {}
        self['strategies'] = ['base']
        self['strategy'] = {}
        self['tenancy'] = {
            #'json': Path.home() / 'tenants.json'
            "dsn": ""
        }
        self["zones"] = {
            "default": {
                "dsn": ""
            }
        }

class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self["mode"] = "DEV"
        self['factory'] = 'TrialFactory'
        self['strategies'].extend(['trial'])


class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = "PROD"
        self['factory'] = 'SqlFactory'
        self['strategies'].extend(['sql'])

class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = "TEST"
        self['factory'] = 'TrialFactory'
        self['strategies'].extend(['trial'])

