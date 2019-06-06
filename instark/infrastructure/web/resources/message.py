import json
from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import MessageSchema
from ..helpers import get_request_filter


class MessageResource(MethodView):

    def __init__(self, resolver) -> None:
        self.notification_coordinator = resolver['NotificationCoordinator']
        self.instark_informer = resolver['InstarkInformer']

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Send message.
        tags:
          - Messages
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Message'
        responses:
          201:
            description: "Send message"
        """

        print('Request Data>>>>>>>>>>>>>', request.data)
        data = MessageSchema().loads(request.data)
        
        print('Data>>>>>>>>>>>>>', data)
        message = self.notification_coordinator.send_message(data)
        print('message>>>>>>>>>>', message)
        json_message = json.dumps(data, sort_keys=True, indent=4)

        return json_message, 201
    
    def get(self) -> Tuple[str, int]:
        """
        ---
        summary: Return all message.
        tags:
          - Messages
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Message'
        """
        domain, limit, offset = get_request_filter(request)

        messages = MessageSchema().dump(
            self.instark_informer.search_messages(domain), many=True)

        return jsonify(messages)
