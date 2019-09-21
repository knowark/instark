from unittest.mock import Mock
from instark.infrastructure.web import ServerApplication
from instark.infrastructure.core import Config


def test_server_application_calls() -> None:
    mock_app = Mock()

    config = {'bind': '%s:%s' % ('0.0.0.0', '8000')}
    server_app = ServerApplication(mock_app, config)
    server_app.load()

    assert server_app is not None
