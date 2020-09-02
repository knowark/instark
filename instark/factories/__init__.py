from typing import Dict, Any
from ..config import Config
from .factory import Factory
from .memory_factory import MemoryFactory
from .sql_factory import SqlFactory
from .check_factory import CheckFactory
from .strategies import build_strategy


def build_factory(config: Config) -> Factory:
    factory = config['factory']
    return {
        'MemoryFactory': lambda config: MemoryFactory(config),
        'CheckFactory': lambda config: CheckFactory(config),
        'SqlFactory': lambda config: SqlFactory(config)
    }[factory](config)
