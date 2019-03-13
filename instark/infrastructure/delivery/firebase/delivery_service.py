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

    def send(self, locator: str, subject: str,
             content: str, payload: list) -> str:
        notification = messaging.Notification(body=content)
        #android_notification = AndroidNotification(sound='default')
        #android_config = AndroidConfig(notification=android_notification)
        #web_notification = WebpushNotification()
        #fcm_options = WebpushFcmOptions(link="https://www.nubark.com")
        #web_configuration = WebpushConfig(
        #    notification=web_notification,
        #    fcm_options=fcm_options)
        message = messaging.Message(
            data={
                'title': 'Message Direct!',
                'body': content,
            },
            #notification=notification,
            # android=android_config,
            #webpush=web_configuration,
            token=locator)
        return messaging.send(message)

    def broadcast(self, str, code: str, subject: str, content: str,
                  payload: list) -> str:
        notification = messaging.Notification(body=content)
        #android_notification = AndroidNotification(sound='default')
        #android_config = AndroidConfig(notification=android_notification)
        #web_notification = WebpushNotification()
        #web_configuration = WebpushConfig(notification=web_notification)
        message = messaging.Message(
        #    notification=notification,
            # android=android_config,
            #webpush=web_configuration,
            data={
                'title': 'Message Direct!',
                'body': content,
            },
            topic=code)
        return messaging.send(message)

    def subscribe(self, code: str, locator: str) -> bool:
        messaging.subscribe_to_topic(tokens=[locator], topic=code)
        return True
