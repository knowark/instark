import os
from typing import cast
from pytest import fixture
from flask import Flask
from datetime import datetime
from flask.testing import FlaskClient
from injectark import Injectark
from instark.infrastructure.core import (
    build_factory, build_config, Config, JwtSupplier)
from instark.infrastructure.cli import Cli
from instark.infrastructure.web import create_app, ServerApplication


@fixture
def app() -> Flask:
    config = build_config("", os.environ.get('INSTARK_MODE', 'DEV'))

    strategy = config['strategy']
    factory = build_factory(config)

    resolver = Injectark(strategy=strategy, factory=factory)

    app = create_app(config, resolver)
    app.testing = True
    app = cast(Flask, app.test_client())

    return app


@fixture
def headers() -> dict:

    payload_dict = {
        "tid": "c5934df0-cab9-4660-af14-c95272a92ab7",
        "uid": "c4e47c69-b7ee-4a06-83bb-b59859478bec",
        "name": "John Doe",
        "email": "johndoe@nubark.com",
        "attributes": {},
        "authorization": {},
        "exp": int(datetime.now().timestamp()) + 5
    }

    jwt_supplier = JwtSupplier('knowark')
    token = jwt_supplier.encode(payload_dict)

    return {"Authorization": (token)}


@fixture
def retrieve_production_conf() -> Config:
    return build_config("", 'PROD')
