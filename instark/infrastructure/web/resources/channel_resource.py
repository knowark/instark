from typing import Any, Dict, Tuple
from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger


class ChannelResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        self.subscription_coordinator = kwargs['subscription_coordinator']
        self.instark_reporter = kwargs['instark_reporter']

    @swagger.operation(
        notes='Retrieve all channels.',
        responseMessages=[
            {"code": 200,
             "message": "Channels are delivered."}
        ]
    )
    def get(self) -> str:
        return self.instark_reporter.search_channels([])

    @swagger.operation(
        notes='Create a new channel.',
        responseMessages=[
            {"code": 201,
             "message": "Created. The channel is now availabe."}
        ]
    )
    def post(self) -> Tuple[str, int]:
        data = request.get_json()
        self.subscription_coordinator.create_channel(data)
        ds = str(data)
        return ds, 200
