from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import SubscriptionSchema


class SubscriptionResource(MethodView):

    def __init__(self, resolver) -> None:
        self.subscription_coordinator = resolver['subscription_coordinator']

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Create subscription.
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
            description: "Success subscription"
        """

        try:
            data = SubscriptionSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        subscription = self.subscription_coordinator.subscribe(data)
        response = 'Subscribe Post: \n channel_id<{0}> - device_id<{1}>'.format(
            subscription.channel_id,
            subscription.device_id,
        )

        return response, 201
  
    def get(self) -> str:
          """
          ---
          summary: Return all devices.
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
              description: "Succesful response"
          """
          try:
              data = SubscriptionSchema().loads(request.data or '{}')
          except ValidationError as error:
              return jsonify(code=400, error=error.messages), 400
          return 201
