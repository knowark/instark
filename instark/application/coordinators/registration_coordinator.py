from typing import Dict, Union, List, Any, cast
from ..models import Device
from ..repositories import DeviceRepository
from ..utilities import DataValidationError, RecordList, EntityNotFoundError


class RegistrationCoordinator:

    def __init__(self, device_repository: DeviceRepository) -> None:
        self.device_repository = device_repository

    #async def register_device(self, registration_dict: Dict[str, str]):
    async def register_device(self, registration_dicts: RecordList) -> None:
        #if 'id' not in registration_dict:
        #    registration_dict['id'] = self.id_service.generate_id()
        #device = Device(**registration_dict)
        #await self.device_repository.add(device)
        #return device
        
        devices = await self.device_repository.add([
            Device(**registration_dict)
            for registration_dict in registration_dicts])
