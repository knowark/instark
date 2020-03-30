from typing import Dict, Union, List, Any, cast
from ..models import Channel, Subscription
from ..repositories import (
    ChannelRepository, DeviceRepository, SubscriptionRepository)
from ..services import DeliveryService
from ..utilities import DataValidationError, RecordList


class SubscriptionCoordinator:
    def __init__(self, channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 subscription_repository: SubscriptionRepository,
                 delivery_service: DeliveryService) -> None:
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.subscription_repository = subscription_repository
        self.delivery_service = delivery_service


    async def create_channel(self, channel_dicts: RecordList) -> None:
        channels = await self.channel_repository.add([
            Channel(**channel_dict)
            for channel_dict in channel_dicts])


    async def subscribe(self, subscription_dicts: RecordList) -> None:
        subscriptions = await self.subscription_repository.add([
            Subscription(**subscription_dict)
            for subscription_dict in subscription_dicts
        ])

        for subscription in subscriptions:
            device, *_ = await self.device_repository.search(
                [('id', '=',  subscription.device_id)])
            channel, *_ = await self.channel_repository.search(
                [('id', '=',  subscription.device_id)])
            self.delivery_service.subscribe(channel.code, device.locator)
            await self.subscription_repository.add(subscription)
            return subscription


    """
    async def subscribe(self, subscription_dict: Dict[str, str]
                        ) -> Subscription:
        device_channel = Subscription(**subscription_dict)
        device, *_ = await self.device_repository.search(
            [('id', '=',  device_channel.device_id)])
        channel, *_ = await self.channel_repository.search(
            [('id', '=',  device_channel.device_id)])
        self.delivery_service.subscribe(channel.code, device.locator)
        await self.subscription_repository.add(device_channel)
        return device_channel """
