from pytest import fixture
from injectark import Injectark
from instark.core import config
from instark.presenters.shell import Shell
from instark.factories import factory_builder, strategy_builder


@fixture
def shell() -> Shell:
    config['factory'] = 'BaseFactory'
    config['strategies'] = ['base']

    strategy = strategy_builder.build(config['strategies'])
    factory = factory_builder.build(config)

    injector = Injectark(strategy, factory)

    return Shell(config, injector)
