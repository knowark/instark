from ..models import Channel, Subscription
from ..repositories import (
    ChannelRepository, DeviceRepository, SubscriptionRepository)
from ..services import IdService, DeliveryService
from .types import ChannelDict, SubscriptionDict


class SubscriptionCoordinator:

    def __init__(self, id_service: IdService,
                 channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 device_channel_repository: SubscriptionRepository,
                 delivery_service: DeliveryService) -> None:
        self.id_service = id_service
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.device_channel_repository = device_channel_repository
        self.delivery_service = delivery_service

    def create_channel(self, channel_dict: ChannelDict) -> None:
        if 'id' not in channel_dict:
            channel_dict['id'] = self.id_service.generate_id()
        channel = Channel(**channel_dict)
        self.channel_repository.add(channel)
        return channel

    def subscribe(self, subscription_dict: SubscriptionDict) -> None:
        if 'id' not in subscription_dict:
            subscription_dict['id'] = self.id_service.generate_id()

        device_channel = Subscription(**subscription_dict)
        device = self.device_repository.get(device_channel.device_id)
        channel = self.channel_repository.get(device_channel.channel_id)
        self.delivery_service.subscribe(channel.code, device.locator)

        self.device_channel_repository.add(device_channel)
        return device_channel
