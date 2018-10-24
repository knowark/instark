from pytest import fixture
from instark.application.models import Device, Channel, Message, DeviceChannel
from instark.application.repositories import (
    ExpressionParser, MemoryDeviceRepository,
    MemoryMessageRepository, MemoryDeviceChannelRepository)
from instark.application.reporters import (
    InstarkReporter, MemoryInstarkReporter)


@fixture
def device_repository():
    parser = ExpressionParser()
    device_repository = MemoryDeviceRepository(parser)
    device_repository.load({
        '001': Device(id='001', name='DEV001', locator='a1b2c3'),
        '002': Device(id='002', name='DEV002', locator='x1y2z3')
    })
    return device_repository


@fixture
def channel_repository():
    parser = ExpressionParser()
    channel_repository = MemoryDeviceRepository(parser)
    channel_repository.load({
        '001': Channel(id='001', name='Channel 1', code='CH001'),
        '002': Channel(id='002', name='Channel 2', code='CH002'),
        '003': Channel(id='003', name='Channel 3', code='CH003')
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
    device_channel_repository = MemoryDeviceChannelRepository(parser)
    device_channel_repository.load({
        '001': DeviceChannel(id='001', device_id='001',
                             channel_id='001'),
        '002': DeviceChannel(id='001', device_id='002',
                             channel_id='001')
    })
    return device_channel_repository


@fixture
def instark_reporter(device_repository, channel_repository,
                     message_repository, device_channel_repository):
    return MemoryInstarkReporter(
        device_repository, channel_repository,
        message_repository, device_channel_repository)
