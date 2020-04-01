from pytest import fixture
from aiohttp import web
from injectark import Injectark
from instark.infrastructure.factories import build_strategy, build_factory
from instark.infrastructure.config import build_config
from instark.infrastructure.web import create_app


@fixture
def app(loop, aiohttp_client):
    """Create app testing client"""
    config = build_config('DEV')
    strategy = build_strategy(config['strategies'])
    factory = build_factory(config)

    resolver = Injectark(strategy, factory)

    app = create_app(config, resolver)

    return loop.run_until_complete(aiohttp_client(app))


@fixture
def headers() -> dict:
    return {
        "From": "john@doe.com",
        "TenantId": "001",
        "UserId": "001",
        "Roles": "user"
    }
