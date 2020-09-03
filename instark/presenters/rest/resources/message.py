from functools import partial
from injectark import Injectark
from ..helpers import MessageSchema
from .resource import Resource


class MessageResource(Resource):
    def __init__(self, resolver: Injectark) -> None:
        manager = resolver['NotificationManager']
        informer = resolver['InstarkInformer']

        super().__init__(
            MessageSchema,
            partial(informer.count, 'message'),
            partial(informer.search, 'message'),
            manager.send_message,
            manager.delete_message
        )
