from .infrastructure.web import create_app, ServerApplication


def main():
    app = create_app()
    ServerApplication(app).run()


if __name__ == '__main__':  # pragma: no cover
    main()
