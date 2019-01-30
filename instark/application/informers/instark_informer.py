from abc import ABC, abstractmethod
from ..repositories import (
    DeviceRepository, ChannelRepository, MessageRepository,
    SubscriptionRepository)
from .types import (
    DeviceDictList, ChannelDictList, SubscriptionDictList,
    MessageDictList, SearchDomain)


class InstarkInformer(ABC):

    @abstractmethod
    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        """Search Instark's devices"""
