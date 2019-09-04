from instark.infrastructure.core.configuration import (
    TrialConfig, DevelopmentConfig
)

def test_trial_config():
    config = TrialConfig()
    assert config['mode'] == 'TEST'


def test_development_config():
    config = DevelopmentConfig()
    assert config['mode'] == 'DEV'
