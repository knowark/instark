import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path


TEST = 'TEST'
DEV = 'DEV'
PROD = 'PROD'


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
        self['secrets'] = {}
        self['strategy'] = {}


class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = TEST
        self['gunicorn'].update({
            'debug': True
        })


class DevelopmentConfig(TrialConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = DEV
        self['gunicorn'].update({
            'debug': True,
            'accesslog': '-',
            'loglevel': 'debug'
        })
        self['authentication'] = {
            "type": "jwt",
            "secret_file": str(Path.home().joinpath('sign.txt'))
        }
        self['secrets'] = {
            "jwt": str(Path.home().joinpath('sign.txt'))
        }
        self['factory'] = 'MemoryFactory'
        self['strategy'].update({
            "QueryParser": {
                "method": "query_parser"
            },
            "CatalogService": {
                "method": "memory_catalog_service"
            },
            "ProvisionService": {
                "method": "memory_provision_service"
            },
            "TenantSupplier": {
                "method": "tenant_supplier"
            },
            "DeviceRepository": {
                "method": "memory_device_repository"
            },
            "ChannelRepository": {
                "method": "memory_channel_repository"
            },
            "SubscriptionRepository": {
                "method": "memory_subscription_repository"
            },
            "MessageRepository": {
                "method": "memory_message_repository"
            },
            "MessageRepository": {
                "method": "memory_message_repository"
            },
            "TenantProvider": {
                "method": "standard_tenant_provider"
            },
            "AuthService": {
                "method": "memory_auth_service"
            },
            "SessionCoordinator": {
                "method": "session_coordinator"
            },
            "RegistrationCoordinator": {
                "method": "registration_coordinator"
            },
            "SubcriptionCoordinator": {
                "method": "subscription_coordinator"
            },
            "NotificationCoordinator": {
                "method": "notification_coordinator"
            },
            "InstarkInformer": {
                "method": "memory_instark_informer"
            },
            "TenantSupplier": {
                "method": "memory_tenant_supplier"
            }
        })


class ProductionConfig(DevelopmentConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = PROD
        self['gunicorn'].update({
            'debug': True,
            'accesslog': '-',
            'loglevel': 'debug'
        })
        self['authentication'] = {
            "type": "jwt",
            "secret_file": str(Path.home().joinpath('sign.txt'))
        }
        self['secrets'] = {
            "jwt": str(Path.home().joinpath('sign.txt'))
        }
        self['factory'] = 'HttpFactory'
        self['strategy'].update({
            "Jwt": {
                "method": "jwt_supplier"
            },
            "Authenticate": {
                "method": "middleware_authenticate"
            }
        })
