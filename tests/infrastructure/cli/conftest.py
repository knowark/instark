from pytest import fixture
from injectark import Injectark
from instark.infrastructure.configuration import build_config#,DevelopmentConfig
from instark.infrastructure.factories import build_strategy, build_factory
from instark.infrastructure.cli import Cli
#from argparse import Namespace

@fixture
def cli() -> Cli:
    """Create app testing client"""
    config = build_config('DEV')
    strategy = build_strategy(config['strategies'], config['strategy'])
    factory = build_factory(config)

    injector = Injectark(strategy, factory)

    return Cli(config, injector)
    
"""@fixture
def cli() -> Cli:
    config = DevelopmentConfig()
    strategy = config["strategy"]
    factory = build_factory(config)

    resolver = Injectark(strategy, factory)

    return Cli(config, resolver)


@fixture
def namespace() -> Namespace:
    return Namespace()"""
