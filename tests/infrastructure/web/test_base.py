from aiohttp import web
from injectark import Injectark
from instark.infrastructure.configuration import build_config
from instark.infrastructure.factories import build_strategy, build_factory
from instark.infrastructure.web import create_app, run_app
from instark.infrastructure.web import base as base_module


def test_create_app():
    config = build_config('DEV')
    strategy = build_strategy(config['strategies'])
    factory = build_factory(config)
    print('FACTORY::', factory)

    injector = Injectark(strategy, factory)

    app = create_app(config, injector)

    assert app is not None
    assert isinstance(app, web.Application)


async def test_run_app(monkeypatch):
    application = None
    called = None
    mock_application = web.Application()

    class MockWeb:
        async def _run_app(self, app, port):
            nonlocal called
            called = True
            nonlocal application
            application = app

    monkeypatch.setattr(
        base_module, 'web', MockWeb())

    await run_app(mock_application)

    assert called
    assert application == mock_application
