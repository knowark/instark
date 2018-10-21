from typing import Any, Dict, Tuple
from flask import request
from flask_restful import Resource


class DeviceResource(Resource):

    def __init__(self, **kwargs: Any) -> None:
        pass

    def get(self) -> str:
        return "List of devices."

    def post(self) -> Tuple[str, int]:
        data = request.get_json()
        ds = str(data)
        return ds, 200
