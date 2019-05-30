"""
Instark entrypoint
"""
import os
import sys
from injectark import Injectark
from .infrastructure.core import build_factory, build_config
from .infrastructure.cli import Cli


def main():  # pragma: no cover
    mode = os.environ.get('INSTARK_DEVELOPMENT', 'DEV')
    config_path = os.environ.get('INSTARK_CONFIG', 'config.json')
    config = build_config(config_path, mode)

    factory = build_factory(config)
    strategy = config['strategy']
    
    resolver = Injectark(strategy=strategy, factory=factory)
    
    Cli(config, resolver)


if __name__ == '__main__':  # pragma: no cover
    main()
