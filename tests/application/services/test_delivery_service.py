from instark.application.services import (
    DeliveryService, MemoryDeliveryService)


def test_delivery_service() -> None:
    methods = DeliveryService.__abstractmethods__  # type: ignore
    assert 'send' in methods


def test_memory_delivery_service_implementation() -> None:
    assert issubclass(MemoryDeliveryService, DeliveryService)


def test_memory_delivery_service_send() -> None:
    delivery_service = MemoryDeliveryService('a1b2c3')
    locator = 'e8j0YSGiE0k:APA91bEz5KQKaS3LfZVZ'
    content = 'Hello World'
    result = delivery_service.send(locator, content)

    assert result == 'a1b2c3'
