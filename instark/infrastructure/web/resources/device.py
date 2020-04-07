from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import DeviceSchema
from ..helpers import get_request_filter
from operator import itemgetter


class DeviceResource:

    def __init__(self, resolver: Injectark) -> None:
        self.resolver = resolver
        self.registration_coordinator = self.resolver['RegistrationCoordinator']
        self.instark_informer = self.resolver['InstarkInformer']

    async def head(self, request) -> int:
        """
        ---
        summary: Return devices HEAD headers.
        tags:
          - Devices
        """
        domain, _, _ = get_request_filter(request)

        headers = {
            'Total-Count': str(await self.instark_informer.count(
                'device', domain))
        }

        return web.Response(headers=headers)

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

        #newlist = sorted(channels, key=lambda k: k['name'])

        devices_order_by_name_asc = sorted(devices, key=itemgetter('name'))

        return web.json_response(devices_order_by_name_asc, dumps=dumps)
        # return web.json_response(devices, dumps=dumps)

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

        data = DeviceSchema(
            many=True).loads(await request.text())

        result = await self.registration_coordinator.register_device(data)

        return web.Response(status=201)

    async def delete(self, request: web.Request):
        """
        ---
        summary: Delete device.
        tags:
          - Devices
        responses:
          204:
            description: "Device deleted."
        """
        ids = []
        uri_id = request.match_info.get('id')
        if uri_id:
            ids.append(uri_id)

        body = await request.text()
        if body:
            ids.extend(loads(await request.text()))

        result = await self.registration_coordinator.delete_device(ids)

        return web.Response(status=204)
