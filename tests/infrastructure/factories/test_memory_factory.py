import inspect
from pytest import fixture
from injectark import Injectark
from questionark.infrastructure.config import Config
from questionark.infrastructure.factories import build_strategy, build_factory


@fixture
def mock_config():
    class MockConfig(Config):
        def __init__(self):
            super().__init__()
            self['factory'] = 'MemoryFactory'

    return MockConfig()


@fixture
def mock_strategy(mock_config):
    return build_strategy(mock_config['strategies'])


def test_memory_factory(mock_config, mock_strategy):
    factory = build_factory(mock_config)
    resolver = Injectark(strategy=mock_strategy, factory=factory)

    for resource in mock_strategy.keys():
        result = resolver.resolve(resource)
        classes = inspect.getmro(type(result))
        assert resource in [item.__name__ for item in classes]
