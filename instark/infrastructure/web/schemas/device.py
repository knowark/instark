from marshmallow import fields
from .entity import EntitySchema


class DeviceSchema(EntitySchema):
    device_id = fields.Str(
        data_key='deviceId', dump_only=True,
        example="9ec44c7c-73d6-4912-8f83-ccff9834132b")
    device_locator = fields.Str(
        required=True, example="e8j0YSGiE0k:APA91bEz5KQKaS3LfZVZjojSs6SLHmbghrAn")
    device_name = fields.Str(
        required=True, example="Android Phone XYZ001")