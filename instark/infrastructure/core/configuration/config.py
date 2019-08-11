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
        self['flask'] = {}
        self['database'] = {}
        self['tenancy'] = {}
        self['secrets'] = {}
        self['strategy'] = {}
        self['environment'] = {
            'home': '/opt/instark'
        }
        self['gunicorn'] = {
            'bind': '%s:%s' % ('0.0.0.0', '8080'),
            'workers': self.number_of_workers(),
            'worker_class': 'gevent',
            'debug': False
        }
    
    def number_of_workers(self):
        return (multiprocessing.cpu_count() * 2) + 1


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
            'loglevel': 'debug',
            'workers': 1
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
            # Query parser
            "QueryParser": {
                "method": "query_parser"
            },

            "CatalogService": {
                "method": "memory_catalog_service"
            },

            # Tenancy
            "TenantProvider": {
                "method": "standard_tenant_provider"
            },
            "TenantSupplier": {
                "method": "memory_tenant_supplier"
            },
            
            "ProvisionService": {
                "method": "memory_provision_service"
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
            # Delivery service
            "DeliveryService": {
                "method": "memory_delivery_service"
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
            "SubscriptionCoordinator": {
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
        self['tenancy'] = {
            'json':  Path.home() / 'tenants.json'
        },
        self['authentication'] = {
            "type": "jwt",
            "secret_file": str(Path.home().joinpath('sign.txt'))
        }
        self['authorization'] = {
            "dominion": "proser"
        }
        self['secrets'] = {
            "jwt": str(Path.home().joinpath('sign.txt'))
        }
        self['factory'] = 'HttpFactory'
        self['strategy'].update({
            "JwtSupplier": {
                "method": "jwt_supplier"
            },
            "Authenticate": {
                "method": "middleware_authenticate"
            },
            "DeliveryService": {
                "method": "firebase_delivery_service"
            },

            # Tenancy

            "TenantProvider": {
                "method": "standard_tenant_provider"
            },

            "TenantSupplier": {
                "method": "json_tenant_supplier"
            },
        })
