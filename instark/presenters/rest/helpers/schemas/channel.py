from marshmallow import fields
from .entity import EntitySchema


class ChannelSchema(EntitySchema):
    name = fields.Str(
        required=True, example="General Notifications")
    code = fields.Str(
        required=True, example="CH001")
