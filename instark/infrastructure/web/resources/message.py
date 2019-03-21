from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import MessageSchema


class MessageResource(MethodView):

    def __init__(self, registry) -> None:
        self.notification_coordinator = registry['notification_coordinator']
        self.spec = registry['spec']

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Publish message.
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
            description: "Message posted"
        """

        try:
            data = MessageSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        message = self.notification_coordinator.send_message(data)
        response = """Message Post: \n recipient_id<{0}> - title<{1}> -
                      content<{2}> - kind<{3}>""".format(
            message.recipient_id,
            message.title,
            message.content,
            message.kind,
        )

        return response, 201
    
    def get(self) -> str:
        """
        ---
        summary: Return all message.
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
            description: "Succesful response"
        """
        try:
            data = MessageSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        return 201
