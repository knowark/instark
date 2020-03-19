from ..models import Device
from ..repositories import DeviceRepository
from ..services import IdService
from .types import RegistrationDict


class RegistrationCoordinator:

    def __init__(self, id_service: IdService,
                 device_repository: DeviceRepository) -> None:
        self.id_service = id_service
        self.device_repository = device_repository

    async def register_device(self, registration_dict: RegistrationDict):
        if 'id' not in registration_dict:
            registration_dict['id'] = self.id_service.generate_id()
        device = Device(**registration_dict)
        await self.device_repository.add(device)
        return device
