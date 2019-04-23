from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..schemas import DeviceSchema


class DeviceResource(MethodView):

    def __init__(self, registry) -> None:
        self.registration_coordinator = registry['registration_coordinator']
        self.spec = registry['spec']

    def put(self) -> Tuple[str, int]:
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
        response = 'Device Post: \n name<{0}> - locator<{1}>'.format(
            device.name,
            device.locator,
        )

        return response, 201
    
    def get(self) -> str:
        """
        ---
        summary: Return all devices.
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
            description: "Succesful response"
        """
        try:
            data = DeviceSchema().loads(request.data or '{}')
        except ValidationError as error:
            return jsonify(code=400, error=error.messages), 400
        return 201
