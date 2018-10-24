from ..models import Channel, Message
from ..repositories import (
    DeviceRepository, MessageRepository)
from ..services import IdService, DeliveryService
from .types import ChannelDict, NotificationDict


class NotificationCoordinator:

    def __init__(self, id_service: IdService,
                 device_repository: DeviceRepository,
                 message_repository: MessageRepository,
                 delivery_service: DeliveryService) -> None:
        self.id_service = id_service
        self.device_repository = device_repository
        self.message_repository = message_repository
        self.delivery_service = delivery_service

    def send_direct_message(self, message_dict: NotificationDict) -> None:
        if 'id' not in message_dict:
            message_dict['id'] = self.id_service.generate_id()

        message = Message(**message_dict)
        device = self.device_repository.get(message.recipient_id)
        sent = self.delivery_service.send(device.locator, message.content)
        if not sent:
            raise ValueError("The message couldn't be sent")

        self.message_repository.add(message)
