from pytest import fixture
from instark.infrastructure.core.configuration import (
    TrialConfig, DevelopmentConfig, ProductionConfig, build_config
)


def test_trial_config():
    config = TrialConfig()
    assert config['mode'] == 'TEST'


def test_development_config():
    config = DevelopmentConfig()
    assert config['mode'] == 'DEV'


@fixture
def custom_config(tmp_path):
    custom_config = tmp_path / "config.json"
    custom_config.write_text("{}")
    return custom_config


def test_build_config(custom_config):
    config = build_config("config.json", "DEV")
    assert isinstance(config, DevelopmentConfig)
    config = build_config("config.json", "PROD")
    assert isinstance(config, ProductionConfig)
    config = build_config(custom_config, "PROD")
    assert isinstance(config, ProductionConfig)
