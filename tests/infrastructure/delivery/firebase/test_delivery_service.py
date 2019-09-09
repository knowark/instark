from instark.infrastructure.delivery.firebase.delivery_service import \
    FirebaseDeliveryService
from instark.infrastructure.delivery.firebase import \
    delivery_service as delivery_service


def test_firebase_delivery_service(monkeypatch):

    called_mock_credentials = False

    class MockCredentials():
        def Certificate(certificate_path):
            nonlocal called_mock_credentials
            called_mock_credentials = True

    called_mock_firebase_admin = False

    def mock_initialize_app(credentials):
        nonlocal called_mock_firebase_admin
        called_mock_firebase_admin = True

    monkeypatch.setattr(
        delivery_service, "credentials", MockCredentials)
    monkeypatch.setattr(
        delivery_service, "initialize_app", mock_initialize_app)

    firebase_delivery_service = FirebaseDeliveryService("")
    assert called_mock_credentials and called_mock_firebase_admin

    called_mock_messaging_notification = False
    called_mock_messaging_send = False
    called_mock_messaging_message = False
    called_mock_subscribe_to_topic = False

    class MockMessaging():
        def Notification(body):
            nonlocal called_mock_messaging_notification
            called_mock_messaging_notification = True

        def Message(data, token=None, topic=None):
            nonlocal called_mock_messaging_message
            called_mock_messaging_message = True

        def send(message):
            nonlocal called_mock_messaging_send
            called_mock_messaging_send = True

        def subscribe_to_topic(tokens, topic):
            nonlocal called_mock_subscribe_to_topic
            called_mock_subscribe_to_topic = True

    monkeypatch.setattr(
        delivery_service, "messaging", MockMessaging)

    firebase_delivery_service.send("", "", "")
    assert called_mock_messaging_notification and called_mock_messaging_send \
        and called_mock_messaging_message

    called_mock_messaging_notification = False
    called_mock_messaging_send = False
    called_mock_messaging_message = False

    firebase_delivery_service.broadcast("", "", "")
    assert called_mock_messaging_notification and called_mock_messaging_send \
        and called_mock_messaging_message

    firebase_delivery_service.subscribe("", "")
    assert called_mock_subscribe_to_topic
