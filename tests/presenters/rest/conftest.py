from pytest import fixture
from injectark import Injectark
from instark.factories import strategy_builder, factory_builder
from instark.presenters.rest import RestApplication
from instark.core import config


@fixture
def app(loop, aiohttp_client):
    """Create app testing client"""
    config['factory'] = 'CheckFactory'
    config['strategies'] = ['base', 'check']

    strategy = strategy_builder.build(config['strategies'])
    factory = factory_builder.build(config)

    injector = Injectark(strategy, factory)

    app = RestApplication(config, injector)

    return loop.run_until_complete(aiohttp_client(app))


@fixture
def headers() -> dict:
    return {
        "Tenant": "Default",
        "From": "john@doe.com",
        "TenantId": "001",
        "UserId": "001",
        "Roles": "user"
    }
