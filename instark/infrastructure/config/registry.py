from abc import ABC, abstractmethod
from ...application.repositories import (
    ExpressionParser, MemoryDeviceRepository)
from ...application.services import StandardIdService
from ...application.coordinators import RegistrationCoordinator
from .config import Config


class Registry(dict, ABC):
    @abstractmethod
    def __init__(self, config: Config) -> None:
        pass


class MemoryRegistry(Registry):

    def __init__(self, config: Config) -> None:
        super().__init__(config)

        parser = ExpressionParser()
        device_repository = MemoryDeviceRepository(parser)

        id_service = StandardIdService()

        registration_coordinator = RegistrationCoordinator(
            id_service, device_repository)

        self['registration_coordinator'] = registration_coordinator
