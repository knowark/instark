import json
from typing import Tuple
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from ..helpers import get_request_filter
from ..schemas import DeviceSchema


class DeviceResource(MethodView):

    def __init__(self, resolver) -> None:
        self.registration_coordinator = resolver['RegistrationCoordinator']
        self.instark_informer = resolver['InstarkInformer']

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

        
        data = DeviceSchema().loads(request.data or '{}')
       
        device = self.registration_coordinator.register_device(data)
        json_device = json.dumps(data, sort_keys=True, indent=4)

        return json_device, 201
    
    def get(self) -> Tuple[str, int]:
        """
        ---
        summary: Return all devices.
        tags:
          - Devices
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Device'
        """
        
        domain, limit, offset = get_request_filter(request)

        devices = DeviceSchema().dump(
            self.instark_informer.search_devices(domain), many=True)

        return jsonify(devices)
