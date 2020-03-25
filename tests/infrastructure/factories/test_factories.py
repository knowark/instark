import inspect
from pytest import fixture, mark
from injectark import Injectark
from instark.infrastructure.factories import build_factory


def test_config(test_data):
    for config in test_data:
        print("FACTORY:::: ", config["factory"])
        factory = build_factory(config)
        resolver = Injectark(
            strategy=config["strategy"], factory=factory)

        for resource in config["strategy"].keys():
            result = resolver.resolve(resource)
            classes = inspect.getmro(type(result))
            assert resource in [item.__name__ for item in classes]
