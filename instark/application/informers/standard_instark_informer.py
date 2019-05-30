from abc import ABC, abstractmethod
from ..repositories import (
    DeviceRepository, ChannelRepository, MessageRepository,
    SubscriptionRepository)
from .types import (
    DeviceDictList, ChannelDictList, SubscriptionDictList,
    MessageDictList, SearchDomain)
from .instark_informer import InstarkInformer


class StandardInstarkInformer(InstarkInformer):

    def __init__(self, device_repository: DeviceRepository,
                 channel_repository: ChannelRepository,
                 message_repository: MessageRepository,
                 device_channel_repository: SubscriptionRepository) -> None:
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.message_repository = message_repository
        self.device_channel_repository = device_channel_repository

    def search_devices(self, domain: SearchDomain) -> DeviceDictList:
        return [vars(device) for device in
                self.device_repository.search(domain)]

    def search_channels(self, domain: SearchDomain) -> ChannelDictList:
        print("DATA****", self.channel_repository.data)
        return [vars(channel) for channel in
                self.channel_repository.search(domain)]

    def search_device_channels(self, domain: SearchDomain
                               ) -> SubscriptionDictList:
        return [vars(device_channel) for device_channel in
                self.device_channel_repository.search(domain)]

    def search_messages(self, domain: SearchDomain) -> MessageDictList:
        return [vars(message) for message in
                self.message_repository.search(domain)]
