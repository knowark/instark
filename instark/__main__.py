import os
from injectark import Injectark
from .infrastructure.web import create_app, ServerApplication
from .infrastructure.core import build_config, build_factory
from .infrastructure.core.config import (
    DevelopmentConfig, ProductionRegistry, MemoryRegistry, Context)


def main():  # pragma: no cover
    ConfigClass = DevelopmentConfig  # type: Type[Config]
    RegistryClass = ProductionRegistry  # type: Type[Registry]

    if os.environ.get('INSTARK_DEVELOPMENT'):
        ConfigClass = DevelopmentConfig
        RegistryClass = MemoryRegistry

    config = ConfigClass()
    factory = build_factory(config)
    strategy = config['strategy']
    resolver = Injectark(strategy=strategy, factory=factory)
    context = Context(config, RegistryClass(config))
    gunicorn_config = config['gunicorn']

    app = create_app(context)
    
    ServerApplication(app, gunicorn_config).run()


if __name__ == '__main__':  # pragma: no cover
    main()
