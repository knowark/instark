from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import DeviceSchema
# from instark.application.coordinators.subscription_coordinator import (
#     SubscriptionCoordinator)
# from ...config import Registry


class DeviceResource(MethodView):

    def __init__(self, registry) -> None:
        self.registration_coordinator = registry['RegistrationCoordinator']
        self.spec = registry['spec']

    def post(self) -> Tuple[str, int]:
        """
        ---
        summary: Create device.
        tags:
          - Devices
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Device'
        responses:
          201:
            description: "Device created"
        """

        try:
            data = DeviceSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        device = self.registration_coordinator.register_device(data)
        print('>>>>>>>>>>>>>> Device >>>>>', device)
        response = 'Device Post: name<{0}> - locator<{1}>'.format(
            device.get('name'),
            device.get('locator'),
        )

        return response, 201
