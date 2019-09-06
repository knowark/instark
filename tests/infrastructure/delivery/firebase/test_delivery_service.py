from instark.infrastructure.delivery.firebase import \
    delivery_service as delivery_service
from instark.infrastructure.delivery.firebase.delivery_service import \
    FirebaseDeliveryService


def test_firebase_delivery_service(monkeypatch):
    called_mock_credentials = False

    class MockCredentials():
        def Certificate(certificate_path):
            nonlocal called_mock_credentials
            called_mock_credentials = True

    called_mock_firebase_admin = False

    class MockFirebaseAdmin():
        def initialize_app(credentials):
            nonlocal called_mock_firebase_admin
            called_mock_firebase_admin = True

    monkeypatch.setattr(
        delivery_service, "credentials", MockCredentials)
    monkeypatch.setattr(
        delivery_service, "firebase_admin", MockFirebaseAdmin)

    firebase_delivery_service = FirebaseDeliveryService("")
    assert called_mock_credentials and called_mock_firebase_admin

