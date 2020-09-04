from marshmallow import Schema, fields, EXCLUDE
from .entity import EntitySchema


class UserSchema(EntitySchema):
    class Meta:
        unknown = EXCLUDE

    user_id = fields.Str(
        data_key='userId', dump_only=True,
        example="f52706c8-ac08-4f9d-a092-8038d1769825")
    user_name = fields.Str(example="Jaime Arango")
    user_email = fields.Str(example="jarango@ops.servagro.com.co")
    user_attributes = fields.Mapping()
    user_authorization = fields.Mapping()
