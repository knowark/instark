from pytest import fixture
from injectark import Injectark
from instark.infrastructure.core import (
    Config, DevelopmentConfig, build_factory)
from instark.infrastructure.cli import Cli
from argparse import Namespace


@fixture
def cli() -> Cli:
    config = DevelopmentConfig()
    strategy = config["strategy"]
    factory = build_factory(config)

    resolver = Injectark(strategy, factory)

    return Cli(config, resolver)


@fixture
def namespace() -> Namespace:
    return Namespace()
