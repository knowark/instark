import sys
import rapidjson as json
import logging
from pathlib import Path
from argparse import ArgumentParser, Namespace
from injectark import Injectark
from migrark import sql_migrate
from typing import List
from ..configuration import Config
from ..web import create_app, run_app #ServerApplication

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Cli:
    def __init__(self, config: Config, resolver: Injectark) -> None:
        self.config = config
        self.resolver = resolver
        #self.registry = resolver
        self.parser = ArgumentParser('Instark')

    async def run(self, argv: List[str]):
        args = await self.parse(argv)
        await args.func(argv)

    async def parse(self, argv: List[str]) -> Namespace:
        subparsers = self.parser.add_subparsers()

        # Provision
        provision_parser = subparsers.add_parser(
            'provision', help='Provision new tenants.')
        provision_parser.add_argument('data', help='JSON encoded tenant.')
        provision_parser.set_defaults(func=self.provision)

        # Serve
        serve_parser = subparsers.add_parser(
            'serve', help='Start HTTP server.')
        serve_parser.add_argument('-p', '--port')
        serve_parser.set_defaults(func=self.serve)

        if len(argv) == 0:
            self.parser.print_help()
            self.parser.exit()
        
        # Migrate
        migrate_parser = subparsers.add_parser(
            'migrate', help='Upgrade tenant schema version.')
        migrate_parser.set_defaults(func=self.migrate)
        migrate_parser.add_argument(
            "-t", "--tenant", help="Target tenant to upgrade",
            required=True)
        migrate_parser.add_argument(
            "-v", "--version", help="Migration version to upgrade",
            required=True)

        if len(argv) == 0:
            self.parser.print_help()
            self.parser.exit()

        return self.parser.parse_args(argv)

    async def serve(self, args: Namespace) -> None:
        logger.info('SERVE')#print('...SERVE:::', args)
        port = args.port or self.config['port']
        app = create_app(self.config, self.resolver)
        #gunicorn_config = self.config['gunicorn']
        await run_app(app,port)
        #ServerApplication(app, gunicorn_config).run()
        logger.info('END SERVE')

    async def provision(self, args: Namespace) -> None:
        logger.info('PROVISION')#print('...PROVISION::::')
        tenant_supplier = self.resolver['TenantSupplier']
        #tenant_dict = {'name': args.name}  # test 1
        tenant_dict = json.loads(args.data)  # test 2
        logger.info("Creating tenant:", tenant_dict)
        tenant_supplier.create_tenant(tenant_dict)
        logger.info('END PROVISION')#print('...END PROVISION::::')

    async def migrate(self, args: Namespace) -> None:
        logger.info(f'MIGRATE: {vars(args)}')
        tenant_supplier = self.injector['TenantSupplier']
        tenant = tenant_supplier.resolve_tenant(args.tenant)
        zone = tenant['zone'] or 'default'

        database_uri = self.config['zones'][zone]['dsn']
        migrations_path = str((Path(__file__).parent.parent / 'data' /
                               'sql' / 'migrations').absolute())
        sql_migrate(database_uri, migrations_path, schema=tenant['slug'],
                    target_version=args.version)
        logger.info('END MIGRATE')

    
