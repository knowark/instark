"""
Instark entrypoint
"""
import os
import sys
from injectark import Injectark
from .infrastructure.core import build_factory, build_config, Config
from .infrastructure.cli import Cli
from .infrastructure.web import create_app, ServerApplication


def main():  # pragma: no cover
    mode = os.environ.get('INSTARK_MODE', 'PROD')
    config_path = os.environ.get('INSTARK_CONFIG', 'config.json')
    config = build_config(config_path, mode)

    factory = build_factory(config)
    strategy = config['strategy']

    resolver = Injectark(strategy=strategy, factory=factory)
    Cli(config, resolver).run(sys.argv[1:])


if __name__ == '__main__':  # pragma: no cover
    main()
