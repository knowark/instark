from typing import Callable
from functools import wraps
from flask import request
from ....application.coordinators import SessionCoordinator
from ...core import JwtSupplier, AuthenticationError, TenantSupplier
# from ..schemas import *


class Authenticate:
    def __init__(self, jwt_supplier: JwtSupplier,
                 tenant_supplier: TenantSupplier,
                 session_coordinator: SessionCoordinator) -> None:
        self.jwt_supplier = jwt_supplier
        self.tenant_supplier = tenant_supplier
        self.session_coordinator = session_coordinator

    def __call__(self, method: Callable) -> Callable:
        @wraps(method)
        def decorator(*args, **kwargs):
            authorization = request.headers.get('Authorization', "")
            token = authorization.replace('Bearer ', '')
            if not token:
                token = request.args.get('access_token')
            try:
                token_payload = self.jwt_supplier.decode(
                    token, verify=False)
                tenant_dict = self.tenant_supplier.get_tenant(
                    token_payload['tid'])
                token_payload = self.jwt_supplier.decode(token, secret=None)
                self.session_coordinator.set_tenant(tenant_dict)
                # user_dict = UserSchema().load(token_payload)
            except Exception as e:
                raise AuthenticationError(
                    "Couldn't authenticate the request.")

            return method(*args, **kwargs)

        return decorator
