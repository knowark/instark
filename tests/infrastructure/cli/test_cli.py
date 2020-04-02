import contextlib
from typing import List
import rapidjson as json
from asyncmock import AsyncMock
from argparse import ArgumentParser, Namespace
from pytest import raises
from instark.infrastructure.cli import Cli
from instark.infrastructure.cli import cli as cli_module


def test_cli_instantiation(cli):
    assert cli is not None


async def test_cli_run(cli):
    mock_parse = AsyncMock()
    cli.parse = mock_parse
    argv: List = []
    await cli.run(argv)

    assert mock_parse.call_count == 1


async def test_cli_parse(cli):
    called = False
    argv = ['serve']
    result = await cli.parse(argv)

    assert result is not None


async def test_cli_parse_empty_argv(cli):
    with raises(SystemExit) as e:
        result = await cli.parse([])


async def test_cli_serve(cli, monkeypatch):
    called = False
    namespace = Namespace(port=8080)  # check port server

    async def mock_run_app(app, port):
        nonlocal called
        called = True

    monkeypatch.setattr(
        cli_module, 'run_app', mock_run_app)

    result = await cli.serve(namespace)

    assert called  # and create_app_called


async def test_cli_provision(cli):
    namespace = Namespace(data=json.dumps({
        'name': 'Knowark'
    }))

    result = await cli.provision(namespace)

    assert result is None


async def test_cli_migrate(cli, monkeypatch):
    called = False
    namespace = Namespace()
    namespace.tenant = 'Default'
    namespace.version = ""

    def mock_sql_migrate_function(
            database_uri, migrations_path, schema, target_version):
        nonlocal called
        called = True

    monkeypatch.setattr(
        cli_module, 'sql_migrate', mock_sql_migrate_function)

    await cli.migrate(namespace)

    assert called

