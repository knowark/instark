from abc import ABC, abstractmethod
from pathlib import Path
from ...application.repositories import (
    ExpressionParser, MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from ...application.services import StandardIdService, MemoryDeliveryService
from ...application.coordinators import (
    RegistrationCoordinator, SubscriptionCoordinator, NotificationCoordinator)
from ...application.informers import MemoryInstarkInformer
from ...infrastructure.delivery import FirebaseDeliveryService
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
        device_channel_repository = MemorySubscriptionRepository(parser)
        message_repository = MemoryMessageRepository(parser)

        id_service = StandardIdService()
        delivery_service = MemoryDeliveryService()

        registration_coordinator = RegistrationCoordinator(
            id_service, device_repository)

        subscription_coordinator = SubscriptionCoordinator(
            id_service, channel_repository, device_repository,
            device_channel_repository, delivery_service)

        notification_coordinator = NotificationCoordinator(
            id_service, channel_repository, device_repository,
            message_repository, delivery_service)

        instark_informer = MemoryInstarkInformer(
            device_repository, channel_repository,
            message_repository, device_channel_repository)

        self['registration_coordinator'] = registration_coordinator
        self['subscription_coordinator'] = subscription_coordinator
        self['notification_coordinator'] = notification_coordinator
        self['instark_informer'] = instark_informer


class ProductionRegistry(Registry):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

        memory_registry = MemoryRegistry(config)

        self.update(memory_registry)

        notification_coordinator = memory_registry[
            'notification_coordinator']

        default_firebase_credentials_path = str(Path.home().joinpath(
            'firebase_credentials.json'))
        firebase_credentials_path = config.get(
            'firebase_credentials_path', default_firebase_credentials_path)
        delivery_service = FirebaseDeliveryService(
            firebase_credentials_path)

        notification_coordinator.delivery_service = delivery_service

        self['notification_coordinator'] = notification_coordinator

        subscription_coordinator = memory_registry[
            'subscription_coordinator']
        subscription_coordinator.delivery_service = delivery_service

        self['subscription_coordinator'] = subscription_coordinator
