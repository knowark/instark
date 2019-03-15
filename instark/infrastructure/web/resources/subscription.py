from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import SubscriptionSchema
# from instark.application.coordinators.subscription_coordinator import (
#     SubscriptionCoordinator)
# from ...config import Registry


class SubscriptionResource(MethodView):

    def __init__(self, registry) -> None:
        self.subscription_coordinator = registry['SubscriptionCoordinator']
        self.spec = registry['spec']

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
        print('>>>>>>>>>>>>>> Device >>>>>', subscription)
        response = 'Subscribe Post: name<{0}> - code<{1}>'.format(
            subscription.get('name'),
            subscription.get('code'),
        )

        return response, 201
