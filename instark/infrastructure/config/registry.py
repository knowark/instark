from abc import ABC, abstractmethod
from ...application.repositories import (
    ExpressionParser, MemoryDeviceRepository, MemoryChannelRepository)
from ...application.services import StandardIdService
from ...application.coordinators import (
    RegistrationCoordinator, SubscriptionCoordinator)
from ...application.reporters import MemoryInstarkReporter
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
        channel_repository = MemoryChannelRepository(parser)

        id_service = StandardIdService()

        registration_coordinator = RegistrationCoordinator(
            id_service, device_repository)

        subscription_coordinator = SubscriptionCoordinator(
            id_service, channel_repository)

        instark_reporter = MemoryInstarkReporter(
            device_repository, channel_repository)

        self['registration_coordinator'] = registration_coordinator
        self['subscription_coordinator'] = subscription_coordinator
        self['instark_reporter'] = instark_reporter
