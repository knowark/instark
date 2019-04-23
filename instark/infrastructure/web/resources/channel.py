from typing import Any, Dict, Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import ChannelSchema


class ChannelResource(MethodView):

    def __init__(self, registry) -> None:
        self.subscription_coordinator = registry['subscription_coordinator']
        self.spec = registry['spec']

    def get(self) -> Tuple[str, int]:
        """
        ---
        summary: Return all channels.
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
            description: "Succesful response"
        """
        try:
            data = ChannelSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        return 201
        
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
        channel = self.subscription_coordinator.create_channel(data)
        response = 'Channel Post: \n name<{0}> - code<{1}>'.format(
            channel.name,
            channel.code,
        )

        return response, 201
