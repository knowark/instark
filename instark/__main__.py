import os
from injectark import Injectark
# from .infrastructure.web import create_app, ServerApplication
from .infrastructure.core import (
    DevelopmentConfig, MemoryRegistry, build_factory, build_config, Context)
from .infrastructure.cli import Cli


def main():  # pragma: no cover
    mode = os.environ.get('INSTARK_DEVELOPMENT', 'DEV')
    config_path = os.environ.get('INSTARK_CONFIG', 'config.json')
    config = build_config(config_path, mode)
    factory = build_factory(config)
    strategy = config['strategy']
    resolver = Injectark(strategy=strategy, factory=factory)
    # context = Context(config, RegistryClass(config))
    # gunicorn_config = config['gunicorn']

    # app = create_app(context, resolver)
    
    # ServerApplication(app, gunicorn_config).run()
    # Cli(config, resolver)


if __name__ == '__main__':  # pragma: no cover
    main()
