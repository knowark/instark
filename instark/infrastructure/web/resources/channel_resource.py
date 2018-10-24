from typing import Any, Dict, Tuple
from flask import request
from flask_restplus import Namespace, Resource, fields


api = Namespace('channels', description='Channels related operations.')

channel = api.model('Channel', {
    'id': fields.String,
    'name': fields.String(required=True),
    'code': fields.String(required=True)
})


@api.doc()
class ChannelResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        self.subscription_coordinator = kwargs['subscription_coordinator']
        self.instark_reporter = kwargs['instark_reporter']

    @api.doc(responses={200: 'Success!'})
    def get(self) -> str:
        return self.instark_reporter.search_channels([])

    @api.doc(responses={204: 'Created.'}, body=channel)
    def post(self) -> Tuple[str, int]:
        data = request.get_json()
        self.subscription_coordinator.create_channel(data)
        ds = str(data)
        return ds, 200
