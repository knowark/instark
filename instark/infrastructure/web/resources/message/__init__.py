from typing import Any, Dict, Tuple
from flask import request
from flask_restful import Resource
from flasgger import swag_from


class MessageResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        self.notification_coordinator = kwargs['notification_coordinator']
        self.instark_reporter = kwargs['instark_reporter']

    @swag_from('get.yml')
    def get(self) -> str:
        return self.instark_reporter.search_messages([])

    @swag_from('post.yml')
    def post(self) -> Tuple[str, int]:
        data = request.get_json()
        self.notification_coordinator.send_message(data)
        ds = str(data)
        return ds, 200
