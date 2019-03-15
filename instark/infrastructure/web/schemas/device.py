from marshmallow import Schema, fields

class DeviceSchema(Schema):
    id = fields.Str(
        required=False, example="9ec44c7c-73d6-4912-8f83-ccff9834132b")
    locator = fields.Str(
        required=True, example="e8j0YSGiE0k:APA91bEz5KQKaS3LfZVZjojSs6SLHmbghrAn")
    name = fields.Str(
        required=True, example="Android Phone XYZ001")