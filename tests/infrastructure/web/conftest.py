#import os
#import jwt
#from typing import cast
#from flask import Flask
#from datetime import datetime
#from flask.testing import FlaskClient
from pytest import fixture
from aiohttp import web
from injectark import Injectark
#from instark.infrastructure.core import JwtSupplier
from instark.infrastructure.factories import build_strategy, build_factory
from instark.infrastructure.configuration import build_config
from instark.infrastructure.cli import Cli
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

"""@fixture
def app(tmp_path) -> Flask:
    config = DevelopmentConfig()
    sign_file = tmp_path / "sign.txt"
    sign_file.write_text("knowark")
    config['secrets'].update({
        "jwt": str(sign_file)
    })
    strategy = config['strategy']
    factory = build_factory(config)

    resolver = Injectark(strategy=strategy, factory=factory)

    app = create_app(config, resolver)
    app.debug = True
    app = cast(Flask, app.test_client())

    return app


@fixture
def headers() -> dict:

    payload_dict = {
        "tid": "1",
        "uid": "1",
        "name": "jjalvarez",
        "email": "jjalvarez@nubark.com",
        "attributes": {},
        "authorization": {},
        "exp": int(datetime.now().timestamp()) + 5
    }

    token = jwt.encode(payload_dict, 'knowark',
                       algorithm='HS256').decode('utf-8')

    return {"Authorization": (token)}"""
