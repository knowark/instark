import firebase_admin
from firebase_admin import credentials, messaging
from ....application.services import DeliveryService


class FirebaseDeliveryService(DeliveryService):
    def __init__(self, certificate_path: str) -> None:
        credentials_ = credentials.Certificate(certificate_path)
        firebase_admin.initialize_app(credentials_)

    def send(self, locator: str, content: str) -> bool:
        "Send method to be implemented."

        message = messaging.Message(
            data={'content': content},
            token=locator)
        return bool(message)
