from typing import Dict, Union, List, Any, cast
from ..models import Channel, Message
from ..repositories import (
    ChannelRepository, DeviceRepository, MessageRepository)
from ..services import IdService, DeliveryService
from ..utilities import DataValidationError, RecordList


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

    #async def send_message(self, message_dict: Dict[str, str]) -> Message:
    async def send_message(self, message_dict: RecordList) -> Message:
        if 'id' not in message_dict:
            message_dict['id'] = self.id_service.generate_id()
            message = Message(**message_dict)
        if message.kind.lower() == 'direct':
            device, *_ = await self.device_repository.search(
                [('id', '=',  message.recipient_id)])
            response = self.delivery_service.send(
                device.locator, str(message.title), message.content)
        else:
            channel, *_ = await self.channel_repository.search(
                [('id', '=',  message.recipient_id)])
            response = self.delivery_service.broadcast(
                channel.code, str(message.title), message.content)

        if not response:
            raise ValueError("The message couldn't be sent")

        message.backend_id = response
        await self.message_repository.add(message)
        return message
