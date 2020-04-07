import inspect
from pytest import fixture
from injectark import Injectark
from instark.infrastructure.config import build_config
from instark.infrastructure.factories import build_strategy, build_factory


@fixture
def mock_config():
    return build_config('DEV')


@fixture
def mock_strategy(mock_config):
    return build_strategy(mock_config['strategies'], mock_config['strategy'])


def test_check_factory(mock_config, mock_strategy):
    factory = build_factory(mock_config)
    resolver = Injectark(strategy=mock_strategy, factory=factory)
    for resource in mock_strategy.keys():
        result = resolver.resolve(resource)
        classes = inspect.getmro(type(result))
        assert resource in [item.__name__ for item in classes]
