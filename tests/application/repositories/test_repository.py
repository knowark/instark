from instark.application.repositories import Repository


def test_repository_methods() -> None:
    methods = Repository.__abstractmethods__
    assert 'add' in methods
    assert 'search' in methods
    assert 'remove' in methods
    assert 'count' in methods
