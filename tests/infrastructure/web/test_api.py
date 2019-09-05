from flask import Flask, request
from json import loads, dumps
from instark.infrastructure.core.configuration import ProductionConfig


def test_production_config_retrieve() -> None:
    assert ProductionConfig()["mode"] == "PROD"


def test_root_resource(app: Flask, headers: dict) -> None:
    response = app.get('/', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None


def test_root_resource_request_none(app: Flask, headers: dict) -> None:
    response = app.get('/?api', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None


def test_invalid_headers(app: Flask) -> None:
    response = app.get('/messages')
    data = loads(str(response.data, 'utf-8'))
    assert data["error"] is not None
