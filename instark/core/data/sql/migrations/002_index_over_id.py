class Migration:
    version = '002'

    def __init__(self, context):
        self.context = context
        self.connection = context['connection']
        self.schema = context['schema']
        self.owner = "instark"
        self.tables = ["channels", "devices", "messages",
                       "subscriptions"]

    def _create_table(self, table):
        return (
            f"CREATE UNIQUE INDEX IF NOT EXISTS {table}_id_key ON "
            f"{self.schema}.{table} ((data->>'id'));"
        )

    def schema_up(self):
        statement = ""
        for table in self.tables:
            statement += self._create_table(table)

        self.connection.execute(statement)

    def schema_down(self):
        """Not implemented."""
