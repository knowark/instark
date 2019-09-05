import os
from typing import cast
from pytest import fixture
from flask import Flask
from datetime import datetime
from flask.testing import FlaskClient
from injectark import Injectark
from instark.infrastructure.core import (
    build_factory, DevelopmentConfig, build_config, Config, JwtSupplier)
from instark.infrastructure.cli import Cli
from instark.infrastructure.web import (
    create_app, ServerApplication, register_error_handler)


@fixture
def app() -> Flask:
    config = DevelopmentConfig()
    strategy = config['strategy']
    factory = build_factory(config)

    resolver = Injectark(strategy=strategy, factory=factory)

    app = create_app(config, resolver)
    app = cast(Flask, app.test_client())

    return app


@fixture
def headers() -> dict:

    payload_dict = {
        "tid": "1",
        "uid": "1",
        "name": "John Doe",
        "email": "johndoe@nubark.com",
        "attributes": {},
        "authorization": {},
        "exp": int(datetime.now().timestamp()) + 5
    }

    jwt_supplier = JwtSupplier('knowark')
    token = jwt_supplier.encode(payload_dict)

    return {"Authorization": (token)}
