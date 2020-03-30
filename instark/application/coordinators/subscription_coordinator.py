from typing import Dict, Union, List, Any, cast
from ..models import Channel, Subscription
from ..repositories import (
    ChannelRepository, DeviceRepository, SubscriptionRepository)
from ..services import IdService, DeliveryService
from ..utilities import DataValidationError, RecordList


class SubscriptionCoordinator:
    def __init__(self, id_service: IdService,
                 channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 subscription_repository: SubscriptionRepository,
                 delivery_service: DeliveryService) -> None:
        self.id_service = id_service
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.subscription_repository = subscription_repository
        self.delivery_service = delivery_service

    #async def create_channel(self, channel_dict: Dict[str, str]) -> Channel:
    async def create_channel(self, channel_dict: RecordList) -> None:
        if 'id' not in channel_dict:
           channel_dict['id'] = self.id_service.generate_id()
        channel = Channel(**channel_dict)
        await self.channel_repository.add(channel)
        return channel

    async def subscribe(self, subscription_dict: Dict[str, str]
                        ) -> Subscription:
        if 'id' not in subscription_dict:
            subscription_dict['id'] = self.id_service.generate_id()
        device_channel = Subscription(**subscription_dict)
        device, *_ = await self.device_repository.search(
            [('id', '=',  device_channel.device_id)])
        channel, *_ = await self.channel_repository.search(
            [('id', '=',  device_channel.device_id)])
        self.delivery_service.subscribe(channel.code, device.locator)
        await self.subscription_repository.add(device_channel)
        return device_channel
