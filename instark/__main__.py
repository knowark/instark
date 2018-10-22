from .infrastructure.web import create_app, ServerApplication
from .infrastructure.config import DevelopmentConfig, MemoryRegistry, Context


def main():
    ConfigClass = DevelopmentConfig  # type: Type[Config]
    RegistryClass = MemoryRegistry  # type: Type[Registry]

    config = ConfigClass()
    context = Context(config, RegistryClass(config))
    gunicorn_config = config['gunicorn']

    app = create_app(context)
    ServerApplication(app, gunicorn_config).run()


if __name__ == '__main__':  # pragma: no cover
    main()
