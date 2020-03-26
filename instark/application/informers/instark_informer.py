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
    
    @abstractmethod
    def search_channels(self, domain: SearchDomain) -> ChannelDictList:
        """Search Instark's devices"""

    @abstractmethod
    def search_device_channels(self, domain: SearchDomain) -> SubscriptionDictList:
        """Search Instark's devices"""

    @abstractmethod
    def search_messages(self, domain: SearchDomain) -> MessageDictList:
        """Search Instark's devices"""

