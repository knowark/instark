from pytest import fixture
from instark.application.models import Device, Channel, Message, Subscription
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository,
    MemoryMessageRepository, MemorySubscriptionRepository)
from instark.application.informers import (
    InstarkInformer, MemoryInstarkInformer)


@fixture
def device_repository():
    parser = ExpressionParser()
    device_repository = MemoryDeviceRepository(parser)
    device_repository.load({
        '001': Device(id='001', name='DEV001', locator_id='1'),
        '002': Device(id='002', name='DEV002', locator_id='2')
    })
    return device_repository


@fixture
def channel_repository():
    parser = ExpressionParser()
    channel_repository = MemoryDeviceRepository(parser)
    channel_repository.load({
        '001': Channel(id='001', name='Channel 1', code='CH001',
                       locator_id='1'),
        '002': Channel(id='002', name='Channel 2', code='CH002',
                       locator_id='2'),
        '003': Channel(id='003', name='Channel 3', code='CH003',
                       locator_id='3')
    })
    return channel_repository


@fixture
def message_repository():
    parser = ExpressionParser()
    message_repository = MemoryMessageRepository(parser)
    message_repository.load({
        '001': Message(id='001', recipient_id='001', kind='Device',
                       content='Super!')
    })
    return message_repository


@fixture
def device_channel_repository():
    parser = ExpressionParser()
    device_channel_repository = MemorySubscriptionRepository(parser)
    device_channel_repository.load({
        '001': Subscription(id='001', device_id='001',
                            channel_id='001'),
        '002': Subscription(id='001', device_id='002',
                            channel_id='001')
    })
    return device_channel_repository


@fixture
def instark_informer(device_repository, channel_repository,
                     message_repository, device_channel_repository):
    return MemoryInstarkInformer(
        device_repository, channel_repository,
        message_repository, device_channel_repository)
