from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import MessageSchema
from instark.application.coordinators.notification_coordinator import (
    NotificationCoordinator)
from ...config import Registry


class MessageResource(MethodView):

    def __init__(self, registry) -> None:
        self.notification_coordinator = registry['NotificationCoordinator']
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
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DA>TA >>>>>', data)
        message = self.notification_coordinator.send_message(data)

        response = """Message Post: recipient_id<{0}> - content<{1}> - 
                      kind<{2}>""".format(
            message.get('recipient_id'),
            message.get('content'),
            message.get('kind', 'Direct')
        )

        return response, 201
