import json
import contextlib
from typing import List
from unittest.mock import AsyncMock
from argparse import ArgumentParser, Namespace
from pytest import raises
from instark.presenters.shell import Shell
from instark.presenters.shell import shell as shell_module


def test_shell_instantiation(shell):
    assert shell is not None


async def test_shell_run(shell):
    mock_parse = AsyncMock()
    shell.parse = mock_parse
    argv: List = []
    await shell.run(argv)

    assert mock_parse.call_count == 1


async def test_shell_parse(shell):
    called = False
    argv = ['serve']
    result = await shell.parse(argv)

    assert result is not None


async def test_shell_parse_empty_argv(shell):
    with raises(SystemExit) as e:
        result = await shell.parse([])


async def test_shell_serve(shell, monkeypatch):
    called = False
    custom_port = None

    class MockRestApplication:
        def __init__(self, config, injector):
            pass

        @staticmethod
        async def run(app, port):
            nonlocal called, custom_port
            called = True
            custom_port = port

    monkeypatch.setattr(
        shell_module, 'RestApplication', MockRestApplication)

    await shell.serve({
        'port': '9201'
    })

    assert called and called
    assert custom_port == 9201


async def test_shell_provision(shell):
    options = {
        'data': json.dumps({
            'id': '001',
            'name': 'Knowark'
        })
    }

    result = await shell.provision(options)

    assert result is None


# async def test_shell_migrate(shell, monkeypatch):
    # called = False
    # options = {
    # 'tenant': 'Default',
    # 'version': ""
    # }

    # def mock_sql_migrate_function(
    # database_uri, migrations_path, schema, target_version):
    # nonlocal called
    # called = True

    # monkeypatch.setattr(
    # shell_module, 'sql_migrate', mock_sql_migrate_function)
    # await shell.migrate(options)

    # assert called
