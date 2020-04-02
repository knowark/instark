from marshmallow import fields
from .entity import EntitySchema


class MessageSchema(EntitySchema):
    # message_id = fields.Str(
    #    data_key='messageId', dump_only=True,
    #    example="01f32c10-6d09-4145-98c5-56d4bf7c1329")
    backend_id = fields.Str(
        data_key="backendId", required=False,
        example="projects/instark/messages/0:154042575")
    recipient_id = fields.Str(
        data_key="recipientId", required=True,
        example="9ec44c7c-73d6-4912-8f83-ccff9834132b")
    title = fields.Str(required=False, example="Message Direct")
    content = fields.Str(required=True, example="Hello World")
    kind = fields.Str(required=True, example="Direct")
    data = fields.Mapping()
    timestamp = fields.Int()
