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

    def message_direct(self, message):
        device = self.device_repository.get(message.recipient_id)
        response = self.delivery_service.send(
            device.locator_id, message.content)
        return response

    def message_channel(self, message):
        channel = self.channel_repository.get(message.recipient_id)
        response = self.delivery_service.broadcast(
            channel.code, message.content)
        return response

    def send_message(self, message_dict: NotificationDict) -> None:
        if 'id' not in message_dict:
            message_dict['id'] = self.id_service.generate_id()

        message = Message(**message_dict)
        if message.kind == 'Direct':
            response = self.message_direct(message)
            # device = self.device_repository.get(message.recipient_id)
            # response = self.delivery_service.send(
            #     device.locator_id, message.content)
        else:
            response = self.message_channel(message)
            # channel = self.channel_repository.get(message.recipient_id)
            # response = self.delivery_service.broadcast(
            #     channel.code, message.content)
        if not response:
            raise ValueError("The message couldn't be sent")

        message.backend_id = response
        self.message_repository.add(message)
