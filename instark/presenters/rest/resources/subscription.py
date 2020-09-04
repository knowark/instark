from functools import partial
from injectark import Injectark
from ..helpers import SubscriptionSchema
from .resource import Resource


class SubscriptionResource(Resource):

    def __init__(self, resolver: Injectark) -> None:
        manager = resolver['SubscriptionManager']
        informer = resolver['InstarkInformer']

        super().__init__(
            SubscriptionSchema,
            partial(informer.count, 'subscription'),
            partial(informer.search, 'subscription'),
            manager.subscribe,
            manager.delete_subscribe
        )
