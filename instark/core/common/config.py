import os
from typing import Dict, Any


Config = Dict[str, Any]

config: Config = {
    'port': int(os.environ.get('INSTARK_PORT', 6291)),
    'auto': bool(os.environ.get('INSTARK_AUTO', True)),
    'factory': os.environ.get('INSTARK_FACTORY', 'SqlFactory'),
    'strategies': os.environ.get(
        'INSTARK_STRATEGIES', 'base,sql').split(','),
    'tenancy': {
        "dsn": os.environ.get('INSTARK_TENANCY_DSN', (
            "postgresql://instark:instark@localhost/instark"))
    },
    'zones': {
        "default": {
            "dsn": os.environ.get('INSTARK_ZONES_DEFAULT_DSN', (
                "postgresql://instark:instark@localhost/instark"))
        }
    },
    'firebase_config_file': os.environ.get(
        'INSTARK_FIREBASE_CONFIG_FILE',
        'proser-2020-firebase-adminsdk-554ie-41811eb8ea.json'),
}
