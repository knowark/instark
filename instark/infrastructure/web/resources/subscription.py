import json
from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..helpers import get_request_filter
from ..schemas import SubscriptionSchema


class SubscriptionResource(MethodView):

    def __init__(self, resolver) -> None:
        self.subscription_coordinator = resolver['SubscriptionCoordinator']
        self.instark_informer = resolver['InstarkInformer']

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Register subscription.
        tags:
          - Subscriptions
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        responses:
          201:
            description: "Subscription created"
        """

        data = SubscriptionSchema().loads(request.data or '{}')
        subscription = self.subscription_coordinator.subscribe(data)
        json_subscription = json.dumps(data, sort_keys=True, indent=4)

        return json_subscription, 201
  
    def get(self) -> Tuple[str, int]:
        """
        ---
        summary: Return all subscriptions.
        tags:
          - Subscriptions
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Subscription'
        """
        
        domain, limit, offset = get_request_filter(request)

        subscriptions = SubscriptionSchema().dump(
            self.instark_informer.search_device_channels(domain), many=True)

        return jsonify(subscriptions)