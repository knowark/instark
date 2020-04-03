from typing import Dict, Union, List, Any, cast
from ..models import Channel, Subscription
from ..repositories import (
    ChannelRepository, DeviceRepository,
    MessageRepository, SubscriptionRepository)
from ..services import DeliveryService
from ..utilities import DataValidationError, RecordList


class SubscriptionCoordinator:
    def __init__(self, channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 message_repository: MessageRepository,
                 subscription_repository: SubscriptionRepository,
                 delivery_service: DeliveryService) -> None:
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.message_repository = message_repository
        self.subscription_repository = subscription_repository
        self.delivery_service = delivery_service

    async def create_channel(self, channel_dicts: RecordList) -> None:
        channels = await self.channel_repository.add([
            Channel(**channel_dict)
            for channel_dict in channel_dicts])

    async def delete_channel(self, channel_ids: List[str]) -> bool:
        print(" channels ids en coordinator      ", channel_ids)
        channels = await self.channel_repository.search(
            [('id', 'in', channel_ids)])
        print(" channels      ", channels)
        if not channels:
            return False
        messages = await self.message_repository.search(
            [('recipient_id', 'in', [
                channel.id for channel in channels]),
                ('kind', '=', 'channel')])
        if messages:
            return False
        subscriptions = await self.subscription_repository.search(
            [('channel_id', 'in', [
                channel.id for channel in channels])])
        await self.subscription_repository.remove(subscriptions)
        return await self.channel_repository.remove(channels)

    async def subscribe(self, subscription_dicts: RecordList) -> None:
        device_ids = [record["device_id"] for record in subscription_dicts]
        channel_ids = [record["channel_id"] for record in subscription_dicts]
        devices = {item.id: item for item in
                   await self.device_repository.search(
                       [('id', 'in',  device_ids)])}
        channels = {item.id: item for item in
                    await self.channel_repository.search(
                        [('id', 'in',  channel_ids)])}
        for subscription_dict in subscription_dicts:
            device = devices[subscription_dict["device_id"]]
            channel = channels[subscription_dict["channel_id"]]
            self.delivery_service.subscribe(channel.code, device.locator)
            await self.subscription_repository.add(
                Subscription(**subscription_dict))

    async def delete_subscribe(self, subscription_ids: List[str]) -> bool:
        subscriptions = await self.subscription_repository.search(
            [('id', 'in', subscription_ids)])
        return await self.subscription_repository.remove(subscriptions)
