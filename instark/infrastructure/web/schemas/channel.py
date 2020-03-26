from marshmallow import fields
from .entity import EntitySchema


class ChannelSchema(EntitySchema):
    channel_id = fields.Str(
        data_key='channelId', dump_only=True,
        example="637250d6-dc57-4d96-9f8a-2697ca5c55c3")
    channel_name = fields.Str(
        required=True, example="General Notifications")
    channel_code = fields.Str(
        required=True, example="CH001")
   