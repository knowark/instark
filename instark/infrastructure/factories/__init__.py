from typing import Dict, Any
from ..configuration import Config
from .factory import Factory
from .memory_factory import MemoryFactory
from .sql_factory import SqlFactory
from .trial_factory import TrialFactory
from .strategies import build_strategy


def build_factory(config: Config) -> Factory:
    factory = config['factory']
    return {
        'MemoryFactory': lambda config: MemoryFactory(config),
        'TrialFactory': lambda config: TrialFactory(config),
        'SqlFactory': lambda config: SqlFactory(config)
    }[factory](config)
