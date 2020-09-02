from instark.application.domain.services import (
    DeliveryService, MemoryDeliveryService)


def test_delivery_service() -> None:
    methods = DeliveryService.__abstractmethods__  # type: ignore
    assert 'send' in methods
    assert 'broadcast' in methods
    assert 'subscribe' in methods


def test_memory_delivery_service_implementation() -> None:
    assert issubclass(MemoryDeliveryService, DeliveryService)


def test_memory_delivery_service_send() -> None:
    delivery_service = MemoryDeliveryService('a1b2c3')
    locator = 'e8j0YSGiE0k:APA91bEz5KQKaS3LfZVZ'
    content = 'Hello World'
    title = 'Message Direct of admin'
    result = delivery_service.send(locator, title, content)

    assert result == 'a1b2c3'


def test_memory_delivery_service_broadcast() -> None:
    delivery_service = MemoryDeliveryService('BROADCAST_MESSAGE')
    code = 'news'
    content = 'Hello World'
    title = 'Message Direct of admin'
    result = delivery_service.broadcast(code, title, content)

    assert result == 'BROADCAST_MESSAGE'


def test_memory_delivery_service_subscribe() -> None:
    delivery_service = MemoryDeliveryService('')
    code = 'news'
    locator = 'e8j0YSGiE0k:APA91bEz5KQKaS3LfZVZ'
    result = delivery_service.subscribe(code, locator)

    assert result is True
