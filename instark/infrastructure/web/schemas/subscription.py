from marshmallow import Schema, fields

class SubscriptionSchema(Schema):
    id = fields.Str(
        required=False, example="637250d6-dc57-4d96-9f8a-2697ca5c55c3")
    code = fields.Str(
        required=True, example="CH001")
    name = fields.Str(
        required=True, example="General Notifications")
