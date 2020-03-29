from pytest import fixture
from injectark import Injectark
from instark.infrastructure.config import build_config
from instark.infrastructure.factories import build_strategy, build_factory
from instark.infrastructure.cli import Cli


@fixture
def cli() -> Cli:
    """Create app testing client"""
    config = build_config('DEV')
    strategy = build_strategy(config['strategies'], config['strategy'])
    factory = build_factory(config)

    injector = Injectark(strategy, factory)

    return Cli(config, injector)
