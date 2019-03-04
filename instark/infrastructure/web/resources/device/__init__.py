from typing import Any, Dict, Tuple
from flask import request
from flask_restful import Resource
from flasgger import swag_from


class DeviceResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        self.registration_coordinator = kwargs['registration_coordinator']
        self.instark_reporter = kwargs['instark_reporter']

    @swag_from('get.yml')
    def get(self) -> str:
        return self.instark_reporter.search_devices([])

    @swag_from('put.yml')
    def put(self) -> Tuple[str, int]:
        data = request.get_json()
        self.registration_coordinator.register_device(data)
        ds = str(data)
        return ds, 200
