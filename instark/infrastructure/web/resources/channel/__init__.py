from typing import Any, Dict, Tuple
from flask import request
from flask_restful import Resource
from flasgger import swag_from


class ChannelResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        self.subscription_coordinator = kwargs['subscription_coordinator']
        self.instark_informer = kwargs['instark_informer']

    @swag_from('get.yml')
    def get(self) -> str:
        return self.instark_informer.search_channels([])

    @swag_from('post.yml')
    def post(self) -> Tuple[str, int]:
        data = request.get_json()
        self.subscription_coordinator.create_channel(data)
        ds = str(data)
        return ds, 200
