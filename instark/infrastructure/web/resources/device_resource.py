# from typing import Any, Dict, Tuple
# from flask import request
# from flask_restful import Resource


# class DeviceResource(Resource):

#     def __init__(self, **kwargs: Any) -> None:
#         self.registration_coordinator = kwargs['registration_coordinator']
#         self.instark_reporter = kwargs['instark_reporter']

#     def get(self) -> str:
#         return self.instark_reporter.search_devices([])

#     def post(self) -> Tuple[str, int]:
#         data = request.get_json()
#         self.registration_coordinator.register_device(data)
#         ds = str(data)
#         return ds, 200
