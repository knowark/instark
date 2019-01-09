from instark.application.informers import InstarkReporter


def test_instark_reporter_instantiation(instark_reporter):
    assert isinstance(instark_reporter, InstarkReporter)


def test_instark_reporter_search_devices(instark_reporter):
    result = instark_reporter.search_devices([])
    assert len(result) == 2


def test_instark_reporter_search_channels(instark_reporter):
    result = instark_reporter.search_channels([])
    assert len(result) == 3


def test_instark_reporter_search_device_channels(instark_reporter):
    result = instark_reporter.search_device_channels([])
    assert len(result) == 2


def test_instark_reporter_search_messages(instark_reporter):
    result = instark_reporter.search_messages([])
    assert len(result) == 1
