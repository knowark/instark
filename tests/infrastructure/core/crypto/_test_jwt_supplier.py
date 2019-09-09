from instark.infrastructure.core import JwtSupplier


def test_jwt_supplier_instantiation(jwt_supplier):
    assert isinstance(jwt_supplier, JwtSupplier)


def test_entire_jwt_supplier(jwt_supplier, payload_dict):
    token = jwt_supplier.encode(payload_dict)
    decoded_payload = jwt_supplier.decode(token)
    assert payload_dict == decoded_payload
