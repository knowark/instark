import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from pathlib import Path

class Config(defaultdict, ABC):
    @abstractmethod
    def __init__(self):
        self["mode"] = "BASE"
        self["port"] = 6291
        self['strategies'] = ['base']
        self['strategy'] = {}
        self["tenancy"] = {
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
        self['factory'] = 'CheckFactory'
        self['strategies'].extend(['check'])



class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = "PROD"
        self["factory"] = "SqlFactory"
        self['strategies'].extend(['sql'])
        self["tenancy"] = {
            "dsn": (
                "postgresql://instark:instark"
                "@localhost/instark")
        }
        self["zones"] = {
            "default": {
                "dsn": ("postgresql://instark:instark"
                        "@localhost/instark")
            }
        }


