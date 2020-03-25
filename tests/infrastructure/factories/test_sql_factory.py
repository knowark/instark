import inspect
from pytest import fixture
from injectark import Injectark
from questionark.infrastructure.config import build_config
from questionark.infrastructure.factories import build_strategy, build_factory
from questionark.infrastructure.factories import sql_factory


@fixture
def mock_config():
    config = build_config('DEV')
    config['factory'] = 'SqlFactory'
    return config


@fixture
def mock_strategy(mock_config):
    strategy = build_strategy(['base', 'sql'])
    return strategy


def test_sql_factory(mock_config, mock_strategy, monkeypatch):
    factory = build_factory(mock_config)
    resolver = Injectark(strategy=mock_strategy, factory=factory)
    for resource in mock_strategy.keys():
        result = resolver.resolve(resource)
        classes = inspect.getmro(type(result))
        assert resource in [item.__name__ for item in classes]
