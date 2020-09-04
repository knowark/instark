from functools import partial
from injectark import Injectark
from ..helpers import ChannelSchema
from .resource import Resource


class ChannelResource(Resource):
    def __init__(self, injector: Injectark) -> None:
        manager = injector['SubscriptionManager']
        informer = injector['InstarkInformer']

        super().__init__(
            ChannelSchema,
            partial(informer.count, 'channel'),
            partial(informer.search, 'channel'),
            manager.create_channel,
            manager.delete_channel
        )
