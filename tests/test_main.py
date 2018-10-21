import instark
from instark.__main__ import main


def test_main(monkeypatch):
    application = None

    def mock_create_app():
        return {'application': 'instark'}

    class MockServerApplication:
        def __init__(self, app):
            self.app = app

        def run(self):
            nonlocal application
            application = self.app

    monkeypatch.setattr(instark.__main__,
                        'create_app', mock_create_app)
    monkeypatch.setattr(instark.__main__,
                        'ServerApplication', MockServerApplication)

    main()

    assert application == {'application': 'instark'}
