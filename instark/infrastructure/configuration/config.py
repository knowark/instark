import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
#from json import loads, JSONDecodeError
from pathlib import Path


"""TEST = 'TEST'
DEV = 'DEV'
PROD = 'PROD'"""


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
        """self['secrets'] = {}   
        self['environment'] = {
            'home': '/opt/instark'
        }
        self['gunicorn'] = {
            'bind': '%s:%s' % ('0.0.0.0', '8080'),
            'workers': 1,
            'worker_class': 'gevent',
            'debug': False
        }"""
        self["zones"] = {
            "default": {
                "dsn": ""
            }
        }

    """def number_of_workers(self):
        return (multiprocessing.cpu_count() * 2) + 1"""

class DevelopmentConfig(TrialConfig):
    def __init__(self):
        super().__init__()
        self["mode"] = "DEV"
        self['factory'] = 'MemoryFactory'
        self['strategies'].extend(['memory'])
        """self["strategy"].update({
            "TenantSupplier": {
                "method": "trial_memory_tenant_supplier"
            }
        })"""


class ProductionConfig(DevelopmentConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = "PROD"
        self['factory'] = 'HttpFactory'
        self['strategies'].extend(['check'])
        #self["tenancy"] = {
        #    "dsn": (
        #        "postgresql://instark:instark"
        #        "@localhost/instark")
        #}
        #self["zones"] = {
        #    "default": {
        #        "dsn": ("postgresql://instark:instark"
        #                "@localhost/instark")
        #    }
        #}
        """self['strategy'].update({

            # Delivery service
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
        })"""

class TrialConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = "TEST"
        self['factory'] = 'TrialFactory'
        self['strategies'].extend(['trial'])
        """self['strategy'].update({
            # Security
            "JwtSupplier": {
                "method": "jwt_supplier"
            },
            "Authenticate": {
                "method": "middleware_authenticate"
            },

            # Query parser
            "QueryParser": {
                "method": "query_parser"
            },

            # Tenancy
            "TenantProvider": {
                "method": "standard_tenant_provider"
            },
            "TenantSupplier": {
                "method": "memory_tenant_supplier"
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
            "IdService": {
                "method": "standard_id_service"
            },
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
            }
        })"""