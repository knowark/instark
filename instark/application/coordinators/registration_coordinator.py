from typing import Dict, Union, List, Any, cast
from ..models import Device
from ..repositories import DeviceRepository
from ..utilities import DataValidationError, RecordList, EntityNotFoundError


class RegistrationCoordinator:

    def __init__(self, device_repository: DeviceRepository) -> None:
        self.device_repository = device_repository

    async def register_device(self, registration_dicts: RecordList) -> None:

        devices = await self.device_repository.add([
            Device(**registration_dict)
            for registration_dict in registration_dicts])

    async def delete_device(self, device_ids: List[str]) -> bool:
        devices = await self.device_repository.search(
            [('id', 'in', device_ids)])
        return await self.device_repository.remove(devices)
