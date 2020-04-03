from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import ChannelSchema
from ..helpers import get_request_filter


class ChannelResource:

    def __init__(self, injector: Injectark) -> None:
        self.injector = injector
        self.subscription_coordinator = self.injector['SubscriptionCoordinator']
        self.instark_informer = self.injector['InstarkInformer']

    async def head(self, request) -> int:
        """
        ---
        summary: Return channels HEAD headers.
        tags:
          - Channels
        """
        domain, _, _ = get_request_filter(request)

        headers = {
            'Total-Count': str(await self.instark_informer.count(
                'channel', domain))
        }

        return web.Response(headers=headers)

    async def get(self, request: web.Request):
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
            await self.instark_informer.search(
                'channel', domain, limit=limit, offset=offset), many=True)

        return web.json_response(channels, dumps=dumps)

    async def put(self, request: web.Request):
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
        channel_records = ChannelSchema(many=True).loads(await request.text())

        result = await self.subscription_coordinator.create_channel(
            channel_records)

        return web.Response(status=201)

    async def delete(self, request: web.Request):
        """
        ---
        summary: Delete channel.
        tags:
          - Channels
        responses:
          204:
            description: "Channel deleted."
        """
        ids = []
        uri_id = request.match_info.get('id')
        if uri_id:
            ids.append(uri_id)

        body = await request.text()
        if body:
            ids.extend(loads(await request.text()))
        print("ids en delete channel   ", ids)
        result = await self.subscription_coordinator.delete_channel(ids)

        return web.Response(status=204)
