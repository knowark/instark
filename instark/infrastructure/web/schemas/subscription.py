from marshmallow import fields
from .entity import EntitySchema


class SubscriptionSchema(EntitySchema):
    # subscription_id = fields.Str(
    #    data_key='messageId', dump_only=True,
    #    example="01f32c10-6d09-4145-98c5-56d4bf7c1329")
    device_id = fields.Str(
        data_key="deviceId", required=True,
        example="9ec44c7c-73d6-4912-8f83-ccff9834132b")
    channel_id = fields.Str(
        data_key="channelId", required=True,
        example="637250d6-dc57-4d96-9f8a-2697ca5c55c3")
