from instark.application.informers import InstarkInformer


def test_instark_informer_instantiation(instark_informer):
    assert isinstance(instark_informer, InstarkInformer)


def test_instark_informer_search_devices(instark_informer):
    result = instark_informer.search_devices([])
    assert len(result) == 2


def test_instark_informer_search_channels(instark_informer):
    result = instark_informer.search_channels([])
    assert len(result) == 3


def test_instark_informer_search_device_channels(instark_informer):
    result = instark_informer.search_device_channels([])
    assert len(result) == 2


def test_instark_informer_search_messages(instark_informer):
    result = instark_informer.search_messages([])
    assert len(result) == 1