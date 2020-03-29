from typing import List, Dict, Any
from .base import base
from .check import check
from .sql import sql


STRATEGIES = {
    'base': base,
    'check': check,
    'sql': sql
}


def build_strategy(strategies: List[str],
                   custom_strategy: Dict[str, Any]={}) -> Dict[str, Any]:
    strategy: Dict[str, Any] = {}
    for name in strategies:
        strategy.update(STRATEGIES[name])
    strategy.update(custom_strategy)
    return strategy
