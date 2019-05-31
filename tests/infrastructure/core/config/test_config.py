from instark.infrastructure.core.config import (
    TrialConfig, DevelopmentConfig
)

def test_trial_config():
    config = TrialConfig()
    assert config['mode'] == 'TEST'


def test_development_config():
    config = DevelopmentConfig()
    assert config['mode'] == 'DEV'
