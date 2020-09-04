from functools import partial
from injectark import Injectark
from ..helpers import DeviceSchema
from .resource import Resource


class DeviceResource(Resource):

    def __init__(self, resolver: Injectark) -> None:
        manager = resolver['RegistrationManager']
        informer = resolver['InstarkInformer']

        super().__init__(
            DeviceSchema,
            partial(informer.count, 'device'),
            partial(informer.search, 'device'),
            manager.register_device,
            manager.delete_device
        )
