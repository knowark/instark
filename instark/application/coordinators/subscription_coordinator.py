from ..models import Channel
from ..repositories import ChannelRepository
from ..services import IdService
from .types import ChannelDict


class SubscriptionCoordinator:

    def __init__(self, id_service: IdService,
                 channel_repository: ChannelRepository) -> None:
        self.id_service = id_service
        self.channel_repository = channel_repository

    def create_channel(self, channel_dict: ChannelDict):
        if 'id' not in channel_dict:
            channel_dict['id'] = self.id_service.generate_id()
        channel = Channel(**channel_dict)
        self.channel_repository.add(channel)
