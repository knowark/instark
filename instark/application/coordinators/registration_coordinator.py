from typing import Dict, Union, List, Any, cast
from ..models import Device, Message, Subscription
from ..services import DeliveryService
from ..repositories import (
    DeviceRepository, MessageRepository, SubscriptionRepository)
from ..utilities import DataValidationError, RecordList, EntityNotFoundError


class RegistrationCoordinator:

    def __init__(self, device_repository: DeviceRepository,
                 message_repository: MessageRepository,
                 subscription_repository: SubscriptionRepository,
                 delivery_service: DeliveryService) -> None:
        self.device_repository = device_repository
        self.message_repository = message_repository
        self.subscription_repository = subscription_repository
        self.delivery_service = delivery_service

    async def register_device(self, registration_dicts: RecordList) -> None:
        print(" reg dicts en registe device    ", registration_dicts)
        devices = await self.device_repository.add([
            Device(**registration_dict)
            for registration_dict in registration_dicts])

    async def delete_device(self, device_ids: List[str]) -> bool:
        devices = await self.device_repository.search(
            [('id', 'in', device_ids)])
        if not devices:
            return False

        messages = await self.message_repository.search(
            [('recipient_id', 'in', [
                device.id for device in devices]),
                ('kind', '=', 'direct')])
        if messages:
            return False
        subscriptions = await self.subscription_repository.search(
            [('device_id', 'in', [
                device.id for device in devices])])
        await self.subscription_repository.remove(subscriptions)
        return await self.device_repository.remove(devices)
