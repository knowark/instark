from ..models import Channel, DeviceChannel
from ..repositories import ChannelRepository, DeviceChannelRepository
from ..services import IdService
from .types import ChannelDict, SubscriptionDict


class SubscriptionCoordinator:

    def __init__(self, id_service: IdService,
                 channel_repository: ChannelRepository,
                 device_channel_repository: DeviceChannelRepository) -> None:
        self.id_service = id_service
        self.channel_repository = channel_repository
        self.device_channel_repository = device_channel_repository

    def create_channel(self, channel_dict: ChannelDict):
        if 'id' not in channel_dict:
            channel_dict['id'] = self.id_service.generate_id()
        channel = Channel(**channel_dict)
        self.channel_repository.add(channel)

    def subscribe(self, subscription_dict: SubscriptionDict):
        if 'id' not in subscription_dict:
            subscription_dict['id'] = self.id_service.generate_id()
        device_channel = DeviceChannel(**subscription_dict)
        self.device_channel_repository.add(device_channel)
