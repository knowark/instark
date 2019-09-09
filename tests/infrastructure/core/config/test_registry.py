from pytest import fixture
from json import dump
from instark.infrastructure.core.configuration import (
    ProductionConfig, ProductionRegistry, Context)
from instark.infrastructure.core.configuration import \
    registry as registry_module


def test_production_registry_context_instantiation(monkeypatch):

    firebase_delivery_service = False

    class MockFirebaseDeliveryService():
        def __init__(self, config):
            nonlocal firebase_delivery_service
            firebase_delivery_service = True

    monkeypatch.setattr(
        registry_module, "FirebaseDeliveryService",
        MockFirebaseDeliveryService)

    production_config = ProductionConfig()

    registry = ProductionRegistry(production_config)
    context = Context(production_config, registry)
    assert context.config == production_config
    assert context.registry == registry
