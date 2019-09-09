from typing import Dict
from pytest import fixture
from datetime import datetime
from instark.infrastructure.core import JwtSupplier


@fixture
def payload_dict() -> Dict:
    return {
        "tid": "c5934df0-cab9-4660-af14-c95272a92ab7",
        "uid": "c4e47c69-b7ee-4a06-83bb-b59859478bec",
        "name": "John Doe",
        "email": "johndoe@nubark.com",
        "attributes": {},
        "authorization": {},
        "exp": int(datetime.now().timestamp()) + 5
    }


@fixture
def jwt_supplier() -> JwtSupplier:
    return JwtSupplier("knowark")
