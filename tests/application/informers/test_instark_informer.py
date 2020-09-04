from pytest import fixture, raises
from instark.application.domain.models import Device, Channel, Message, Subscription
from instark.application.domain.common import (
    QueryParser, Tenant, StandardTenantProvider, Tenant,
    AuthProvider, StandardAuthProvider, User, QueryDomain)
from instark.application.domain.repositories import (
    DeviceRepository, MemoryDeviceRepository,
    ChannelRepository, MemoryChannelRepository,
    MessageRepository, MemoryMessageRepository,
    SubscriptionRepository, MemorySubscriptionRepository)
from instark.application.informers import (
    InstarkInformer, StandardInstarkInformer)


@fixture
def parser():
    return QueryParser()


@fixture
def auth_provider() -> AuthProvider:
    auth_provider = StandardAuthProvider()
    auth_provider.setup(User(id='001', name='johndoe'))
    return auth_provider


@fixture
def tenant_provider():
    tenant_provider = StandardTenantProvider()
    tenant_provider.setup(Tenant(name="Default"))
    return tenant_provider


@fixture
def device_repository(
        tenant_provider, auth_provider, parser) -> DeviceRepository:
    device_repository = MemoryDeviceRepository(
        parser, tenant_provider, auth_provider)
    device_repository.load({
        'default': {
            '001': Device(**{'id': '001', 'name': 'DEV001', 'locator': '1'}),
            '002': Device(**{'id': '002', 'name': 'DEV002', 'locator': '2'})
        }
    })
    return device_repository


@fixture
def channel_repository(
        tenant_provider, auth_provider, parser) -> ChannelRepository:
    channel_repository = MemoryChannelRepository(
        parser, tenant_provider, auth_provider)
    channel_repository.load({
        'default': {
            '001': Channel(id='001', name='Channel 1', code='CH001'),
            '002': Channel(id='002', name='Channel 2', code='CH002'),
            '003': Channel(id='003', name='Channel 3', code='CH003')

        }
    })
    return channel_repository


@fixture
def message_repository(
        tenant_provider, auth_provider, parser) -> MessageRepository:
    message_repository = MemoryMessageRepository(
        parser, tenant_provider, auth_provider)
    message_repository.load({
        'default': {
            '001': Message(id='001', recipient_id='001', kind='direct',
                           content='Super!', title='Hello')
        }
    })
    return message_repository


@fixture
def subscription_repository(
        tenant_provider, auth_provider, parser) -> SubscriptionRepository:
    subscription_repository = MemorySubscriptionRepository(
        parser, tenant_provider, auth_provider)
    subscription_repository.load({
        'default': {
            '001': Subscription(**{'id': '001', 'device_id': '001',
                                   'channel_id': '001'}),
            '002': Subscription(**{'id': '001', 'device_id': '002',
                                   'channel_id': '001'})
        }
    })
    return subscription_repository


@fixture
def instark_informer(device_repository: DeviceRepository,
                     channel_repository: ChannelRepository,
                     message_repository: MessageRepository,
                     subscription_repository: SubscriptionRepository
                     ) -> InstarkInformer:
    return StandardInstarkInformer(
        device_repository,
        channel_repository,
        message_repository,
        subscription_repository)


async def test_instark_informer_search_devices(
        instark_informer: InstarkInformer) -> None:
    domain: QueryDomain = []
    devices = await instark_informer.search('device', domain)
    assert len(devices) == 2


async def test_instark_informer_search_channels(
        instark_informer: InstarkInformer) -> None:
    domain: QueryDomain = []
    channels = await instark_informer.search('channel', domain)
    assert len(channels) == 3


async def test_instark_informer_subscriptions(
        instark_informer: InstarkInformer) -> None:
    domain: QueryDomain = []
    subscriptions = await instark_informer.search('subscription', domain)
    assert len(subscriptions) == 2


async def test_instark_informer_search_messages(
        instark_informer: InstarkInformer) -> None:
    domain: QueryDomain = []
    messages = await instark_informer.search('message', domain)
    assert len(messages) == 1


async def test_instark_informer_count_messages(
        instark_informer: InstarkInformer) -> None:
    messages_count = await instark_informer.count('message')
    assert messages_count == 1
