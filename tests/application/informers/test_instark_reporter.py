from instark.application.informers.instark_informer import InstarkInformer
from .conftest import *


def test_instark_informer_instantiation(instark_informer):
    assert isinstance(instark_informer, InstarkInformer)


async def test_instark_informer_search_devices(instark_informer):
    result = await instark_informer.search_devices([])
    assert len(result) == 2


async def test_instark_informer_search_channels(instark_informer):
    result = await instark_informer.search_channels([])
    assert len(result) == 3


async def test_instark_informer_search_device_channels(instark_informer):
    result = await instark_informer.search_device_channels([])
    assert len(result) == 2


async def test_instark_informer_search_messages(instark_informer):
    result = await instark_informer.search_messages([])
    assert len(result) == 1
