from abc import ABC, abstractmethod
from typing import List, Union, Dict, Any
from ..models import Device, Channel, Message, Subscription
from ..repositories import (
    DeviceRepository, ChannelRepository, MessageRepository,
    SubscriptionRepository)
from ..utilities import RecordList, QueryDomain


class InstarkInformer(ABC):
    @abstractmethod
    async def search(self,
                     model: str,
                     domain: QueryDomain = None,
                     limit: int = 0,
                     offset: int = 0) -> RecordList:
        """Returns a list of <<model>> dictionaries matching the domain"""

    #@abstractmethod
    #async def count(self,
    #                model: str,
    #                domain: QueryDomain = None) -> int:
    #    """Returns a the <<model>> records count"""


class StandardInstarkInformer(InstarkInformer):
    def __init__(self, device_repository: DeviceRepository,
                channel_repository: ChannelRepository,
                message_repository: MessageRepository,
                subscription_repository: SubscriptionRepository
    ) -> None:
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.message_repository = message_repository
        self.subscription_repository = subscription_repository

    async def search(self,
                    model: str,
                    domain: QueryDomain = None,
                    limit: int = 1000,
                    offset: int = 0) -> RecordList:
        repository = getattr(self, f'{model}_repository')
        return [vars(entity) for entity in
            await repository.search(
                domain or [], limit=limit, offset=offset)]

    """async def count(self,
                model: str,
                domain: QueryDomain = None) -> int:
        repository = getattr(self, f'{model}_repository')
        return await repository.count(domain or [])"""

  
    #@abstractmethod
    #def search_devices(self, domain: SearchDomain) -> DeviceDictList:
    #    """Search Instark's devices"""
    #
    #@abstractmethod
    #def search_channels(self, domain: SearchDomain) -> ChannelDictList:
    #    """Search Instark's devices"""
    #
    #@abstractmethod
    #def search_device_channels(self, domain: SearchDomain) -> SubscriptionDictList:
    #    """Search Instark's devices"""
    #
    #@abstractmethod
    #def search_messages(self, domain: SearchDomain) -> MessageDictList:
    #    """Search Instark's devices"""



      #async def search_devices(self, domain: SearchDomain) -> DeviceDictList:
    #    return [vars(device) for device in
    #            await self.device_repository.search(domain)]
    #
    #async def search_channels(self, domain: SearchDomain) -> ChannelDictList:
    #    return [vars(channel) for channel in
    #            await self.channel_repository.search(domain)]
    #
    #async def search_device_channels(self, domain: SearchDomain
    #                           ) -> SubscriptionDictList:
    #    return [vars(device_channel) for device_channel in
    #            await self.device_channel_repository.search(domain)]
    #
    #async def search_messages(self, domain: SearchDomain) -> MessageDictList:
    #    return [vars(message) for message in
    #            await self.message_repository.search(domain)]
