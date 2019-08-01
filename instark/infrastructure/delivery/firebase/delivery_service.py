from ....application.services import DeliveryService
import firebase_admin
from firebase_admin import credentials, messaging
# import for create Android notification
from firebase_admin.messaging import AndroidConfig, AndroidNotification
# import for create Web notification
from firebase_admin.messaging import WebpushConfig, WebpushNotification
from firebase_admin.messaging import WebpushFcmOptions


class FirebaseDeliveryService(DeliveryService):
    def __init__(self, certificate_path: str) -> None:
        credentials_ = credentials.Certificate(certificate_path)
        firebase_admin.initialize_app(credentials_)

    def send(self, locator: str, title: str, content: str) -> str:
        notification = messaging.Notification(body=content)
        message = messaging.Message(
            data={
                'title': title,
                'body': content,
            },
            token=locator)
        return messaging.send(message)

    def broadcast(self, code: str, title: str, content: str) -> str:
        notification = messaging.Notification(body=content)
        message = messaging.Message(
            data={
                'title': title,
                'body': content,
            },
            topic=code)
        return messaging.send(message)

    def subscribe(self, code: str, locator: str) -> bool:
        messaging.subscribe_to_topic(tokens=[locator], topic=code)
        return True
