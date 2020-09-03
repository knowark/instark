from injectark import StrategyBuilder
from .base import base
from .check import check
from .sql import sql


strategy_builder = StrategyBuilder({
    'base':  base,
    'check':  check,
    'sql': sql
})
