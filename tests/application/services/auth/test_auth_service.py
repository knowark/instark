from pytest import fixture, raises
from instark.application.services import (
    AuthService, StandardAuthService, User)
from instark.application.utilities import (AuthenticationError,
                                            AuthorizationError)


def test_auth_service_repository_methods():
    abstract_methods = AuthService.__abstractmethods__

    assert 'setup' in abstract_methods
    assert 'user' in abstract_methods
    assert 'roles' in abstract_methods
    assert 'validate_roles' in abstract_methods


@fixture
def auth_service() -> StandardAuthService:
    # Given a memory auth_service has been created
    #dominion = 'maindominion'
    #auth_service = StandardAuthService(dominion, User(name="eecheverry"))
    auth_service = StandardAuthService()
    auth_service.setup(User(name="eecheverry"))
    return auth_service


@fixture
def loaded_auth_service(auth_service) -> StandardAuthService:
    auth_service.load({
        ("easb123")
    })
    return auth_service


def test_standard_auth_service(auth_service):
    assert issubclass(StandardAuthService, AuthService)
    assert isinstance(auth_service, AuthService)


def test_standard_auth_service_verify(auth_service):
    # Given a user
    user = User(name="asb123")
    # When a user is given
    auth_service.setup(user)
    # Then the user will be set
    assert auth_service.user is not None


def test_standard_auth_get_user(auth_service):
    # When the get_user method is called
    user = auth_service.user
    # Then the current request user is returned
    assert user.name == "eecheverry"


def test_standard_auth_roles_authenticated(auth_service):
    # When the get_roles method is called and there is
    # a valid authentication
    auth_service.setup(User(
        name='john',
        roles=['admin']))
    roles = auth_service.roles
    assert roles == ['admin']


def test_standard_auth_get_roles_no_authenticated(auth_service):
    # When the get_roles method is called and there isn't
    # a valid authentication
    #auth_service.state.user = None
    auth_service.setup(None)
    with raises(AuthenticationError):
        roles = auth_service.roles


def test_standard_auth_validate_roles_correct_roles(auth_service):
    # Given a list of roles, a list of required roles and a
    # authenticated user
    auth_service.setup(User(name='john',  roles=['MONITOR']))
    required_roles = ["MONITOR", "ADMIN"]
    # When a list of roles is set
    # Then the roles are validated
    auth_service.validate_roles(required_roles)
    assert 'MONITOR' in auth_service.roles


def test_standard_auth_validate_roles_incorrect_roles(auth_service):
    # Given a list of roles, a list of required roles and a
    # authenticated user
    """
    auth_service.state.user = User(name='john',  authorization={
        'maindominion': {
            'roles': ['monitor']
        }
    })"""
    auth_service.setup(User(name='john',  roles=['MONITOR']))
    required_roles = ["ADMIN"]
    # When a list of roles is setted
    # Then an authorizationerror is raised
    with raises(AuthorizationError):
        auth_service.validate_roles(required_roles)

def test_standard_auth_raises_if_user_not_set(auth_service):
    # Given an auth service without user
    auth_service.setup(None)
    # When the user property is invoked
    # Then an AuthenticationError is raised
    with raises(AuthenticationError):
        user = auth_service.user
