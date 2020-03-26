from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import ChannelSchema
from ..helpers import get_request_filter


class ChannelResource:

    def __init__(self, resolver: Injectark) -> None:
        #self.subscription_coordinator = resolver['SubscriptionCoordinator']
        self.resolver = resolver
        self.instark_informer = resolver['InstarkInformer']

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
                'answer', domain))
        }

        return web.Response(headers=headers)

    #def get(self) -> Tuple[str, int]:
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
                'channel',domain, limit=limit, offset=offset), many=True)

        #return jsonify(channels)
        return web.json_response(channels, dumps=dumps)

    #def post(self) -> Tuple[str, int]:
    async def post(self, request: web.Request):

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

        data = ChannelSchema().loads( await request.data)

        channel = await self.subscription_coordinator.create_channel(data)

        #return json_channel, 201
        return web.Response(status=201)
