from flask import Flask, request
from instark.infrastructure.core.configuration import ProductionConfig


def test_production_config_retrieve(retrieve_production_conf) -> None:
    assert isinstance(retrieve_production_conf, ProductionConfig)


def test_root_resource(app: Flask, headers: dict) -> None:
    response = app.get('/', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None


def test_root_resource_request_none(app: Flask, headers: dict) -> None:
    response = app.get('/?api', headers=headers)
    data = str(response.data, 'utf-8')
    assert data is not None
