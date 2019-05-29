from typing import Callable
from functools import wraps
from flask import request
from ....application.coordinators import SessionCoordinator
from ...core import JwtSupplier, AuthenticationError, TenantSupplier
from ..schemas import *

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

