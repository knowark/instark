import firebase_admin
from firebase_admin import credentials, messaging
from ....application.services import DeliveryService


class FirebaseDeliveryService(DeliveryService):
    def __init__(self, certificate_path: str) -> None:
        credentials_ = credentials.Certificate(certificate_path)
        firebase_admin.initialize_app(credentials_)

    def send(self, locator: str, content: str) -> str:
        "Send method to be implemented."

        notification = messaging.Notification(body=content)

        message = messaging.Message(
            notification=notification,
            token=locator)

        response = messaging.send(message)

        return response
