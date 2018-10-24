# from typing import Any, Dict, Tuple
# from flask import request
# from flask_restful import Resource


# class SubscriptionResource(Resource):

#     def __init__(self, **kwargs: Any) -> None:
#         self.subscription_coordinator = kwargs['subscription_coordinator']
#         self.instark_reporter = kwargs['instark_reporter']

#     def get(self) -> str:
#         return self.instark_reporter.search_device_channels([])

#     def post(self) -> Tuple[str, int]:
#         data = request.get_json()
#         self.subscription_coordinator.subscribe(data)
#         ds = str(data)
#         return ds, 200
