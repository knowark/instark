import json
from typing import Any, Dict, Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..helpers import get_request_filter
from ..schemas import ChannelSchema


class ChannelResource(MethodView):

    def __init__(self, resolver) -> None:
        self.subscription_coordinator = resolver['SubscriptionCoordinator']
        self.instark_informer = resolver['InstarkInformer']

    def get(self) -> Tuple[str, int]:
        """
        ---
        summary: Return all channels.
        tags:
          - Channels
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Channel'
        """

        domain, limit, offset = get_request_filter(request)

        channels = ChannelSchema().dump(
            self.instark_informer.search_channels(domain), many=True)

        return jsonify(channels)

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Register channel.
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

        data = ChannelSchema().loads(request.data)

        channel = self.subscription_coordinator.create_channel(data)
        json_channel = json.dumps(data, sort_keys=True, indent=4)

        return json_channel, 201
