from typing import Any, Dict, Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import ChannelSchema
from instark.application.coordinators.subscription_coordinator import (
    SubscriptionCoordinator)


class ChannelResource(MethodView):

    def __init__(self, registry) -> None:
        self.subscription_coordinator = registry['subscription_coordinator']
        self.spec = registry['spec']

    def get(self) -> str:
        return "Here code for get"

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Create channel.
        tags:
          - Channels
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Channel'
        responses:
          201:
            description: "Channel created"
        """

        try:
            data = ChannelSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        print('>>>>>>>>>>>>>> Data >>>>>', data)
        channel = self.subscription_coordinator.create_channel(data)
        # channel = SubscriptionCoordinator.create_channel(request.data, '')
        print('>>>>>>>>>>>>>> Channel >>>>>', channel)
        response = 'Channel Post: name<{0}> - code<{1}>'.format(
            channel.get('name'),
            channel.get('code'),
        )

        return response, 201
