import contextlib
from typing import List
import rapidjson as json
from asyncmock import AsyncMock
from argparse import ArgumentParser, Namespace
from pytest import raises
#from unittest.mock import Mock, call
from instark.infrastructure.cli import Cli
from instark.infrastructure.cli import cli as cli_module
#from io import StringIO


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
    namespace = Namespace(port=8080) #check port server
    
    """class MockServerApplication:
        def __init__(self, app, options):
            pass

        def run(self):
            nonlocal called
            called = True

    create_app_called = False

    def mock_create_app_function(config, resolver):
        nonlocal create_app_called
        create_app_called = True

    monkeypatch.setattr(
        cli_module, 'ServerApplication', MockServerApplication)
    monkeypatch.setattr(
        cli_module, 'create_app', mock_create_app_function)"""

    async def mock_run_app(app, port):
        nonlocal called
        called = True

    monkeypatch.setattr(
        cli_module, 'run_app', mock_run_app)

    result = await cli.serve(namespace)

    assert called #and create_app_called

async def test_cli_provision(cli):
    namespace = Namespace(data=json.dumps({
        'name': 'Knowark'
    }))

    result = await cli.provision(namespace)

    assert result is None
    """namespace.name = "custom"
    cli.provision(namespace)
    tenants = cli.resolver["TenantSupplier"].search_tenants("")

    assert len(tenants) == 2
    assert tenants[0]["name"] == "custom"

    print("TENANTS::::", tenants)"""

"""async def test_cli_migrate(cli, monkeypatch):
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

    assert called"""

