from typing import Dict, Union, List, Any, cast
from ..domain.models import Channel, Message
from ..domain.repositories import (
    ChannelRepository, DeviceRepository, MessageRepository)
from ..domain.services import DeliveryService
from ..domain.common import DataValidationError, RecordList


class NotificationManager:

    def __init__(self, channel_repository: ChannelRepository,
                 device_repository: DeviceRepository,
                 message_repository: MessageRepository,
                 delivery_service: DeliveryService) -> None:
        self.channel_repository = channel_repository
        self.device_repository = device_repository
        self.message_repository = message_repository
        self.delivery_service = delivery_service

    async def send_message(self, message_dicts: RecordList) -> None:

        messages = await self.message_repository.add([
            Message(**message_dict)
            for message_dict in message_dicts
        ])

        for message in messages:
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

    async def delete_message(self, message_ids: List[str]) -> bool:
        messages = await self.message_repository.search(
            [('id', 'in', message_ids)])
        return await self.message_repository.remove(messages)
