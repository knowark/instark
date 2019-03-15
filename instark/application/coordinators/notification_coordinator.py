from ..models import Channel, Message
from ..repositories import (
    ChannelRepository, DeviceRepository, MessageRepository)
from ..services import IdService, DeliveryService
from .types import ChannelDict, NotificationDict


class NotificationCoordinator:

    def __init__(self, id_service: IdService,
                 channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 message_repository: MessageRepository,
                 delivery_service: DeliveryService) -> None:
        self.id_service = id_service
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.message_repository = message_repository
        self.delivery_service = delivery_service

    def send_message(self, message_dict: NotificationDict) -> None:
        if 'id' not in message_dict:
            message_dict['id'] = self.id_service.generate_id()

        message = Message(**message_dict)

        if message.kind == 'Direct':
            device = self.device_repository.get(message.recipient_id)
            response = self.delivery_service.send(
                device.locator, message.subject, message.content)
        else:
            channel = self.channel_repository.get(message.recipient_id)
            response = self.delivery_service.broadcast(
                channel.code, message.subject, message.content)

        if not response:
            raise ValueError("The message couldn't be sent")

        message.backend_id = response
        self.message_repository.add(message)
