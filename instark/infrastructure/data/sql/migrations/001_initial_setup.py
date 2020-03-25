class Migration:
    version = '001'

    def __init__(self, context):
        self.context = context
        self.connection = context['connection']
        self.schema = context['schema']
        self.owner = "instark"
        self.tables = [] #["questionnaires", "questions", "options",
        #               "assessments", "answers"]

    def _create_table(self, table):
        return (
            f"CREATE TABLE IF NOT EXISTS {self.schema}.{table} "
            "(data JSONB);"
            f"ALTER TABLE {self.schema}.{table} OWNER TO {self.owner};"
        )

    def schema_up(self):
        statement = ""
        for table in self.tables:
            statement += self._create_table(table)

        with self.connection.cursor() as cursor:
            cursor.execute(statement)

    def schema_down(self):
        """Not implemented."""
