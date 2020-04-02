from marshmallow import fields
from .entity import EntitySchema


class ChannelSchema(EntitySchema):
    # id = fields.Str(
    #    data_key='id', dump_only=True,
    #    example="637250d6-dc57-4d96-9f8a-2697ca5c55c3")
    name = fields.Str(
        required=True, example="General Notifications")
    code = fields.Str(
        required=True, example="CH001")
