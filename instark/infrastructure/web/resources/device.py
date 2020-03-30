from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import DeviceSchema
from ..helpers import get_request_filter


class DeviceResource:

    def __init__(self, resolver: Injectark) -> None:
        self.resolver = resolver
        self.registration_coordinator = self.resolver['RegistrationCoordinator']
        self.instark_informer = self.resolver['InstarkInformer']

    async def head(self, request) -> int:
        """
        ---
        summary: Return answers HEAD headers.
        tags:
          - Answers
        """
        domain, _, _ = get_request_filter(request)

        headers = {
            'Total-Count': str(await self.instark_informer.count(
                'device', domain))
        }

        return web.Response(headers=headers)

    #def get(self) -> Tuple[str, int]:
    async def get(self, request: web.Request):
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
            await self.instark_informer.search(
                'device', domain, limit=limit,
                offset=offset), many=True)

        #return jsonify(devices)
        return web.json_response(devices, dumps=dumps)
    
    #async def put(self) -> Tuple[str, int]:
    async def put(self, request: web.Request):

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
        
        #data = DeviceSchema().loads(request.data or '{}')
        data = DeviceSchema(
            many=True).loads(await request.text())
       
        result = await self.registration_coordinator.register_device(data)

        #return json_device, 201
        return web.Response(status=201)
    
  
