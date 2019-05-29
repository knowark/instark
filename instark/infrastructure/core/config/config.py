import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path


TEST = 'TEST'
DEV = 'DEV'


class Config(defaultdict, ABC):
    @abstractmethod
    def __init__(self):
        self['mode'] = 'BASE'
        self['environment'] = {
            'home': '/opt/instark'
        }
        self['gunicorn'] = {
            'bind': '%s:%s' % ('0.0.0.0', '8080'),
            'workers': 1,
            'worker_class': 'gevent',
            'debug': False
        }
        self['flask'] = {}
        self['tenancy'] = {
            'json': Path.home() / 'tenants.json'
        }
        self['database'] = {}
        self['tokens'] = {
            'access': {
                'algorithm': 'HS256',
                'secret': 'DEVSECRET123',
                'lifetime': 86400
            },
            'tenant': {
                'algorithm': 'HS256',
                'secret': 'DEVSECRET123',
                'lifetime': 86400
            },
            'refresh': {
                'algorithm': 'HS256',
                'secret': 'DEVSECRET123',
                'lifetime': 604800,
                'threshold': 86400
            }
        }


class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = TEST
        self['gunicorn'].update({
            'debug': True
        })


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = DEV
        self['gunicorn'].update({
            'debug': True
        })
