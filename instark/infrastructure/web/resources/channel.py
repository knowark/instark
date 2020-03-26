from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import ChannelSchema
from ..helpers import get_request_filter


class ChannelResource:

    def __init__(self, resolver: Injectark) -> None:
      self.resolver = resolver
      self.subscription_coordinator = self.resolver['SubscriptionCoordinator']
      self.instark_informer = self.resolver['InstarkInformer']

    async def head(self, request) -> int:
      domain, _, _ = get_request_filter(request)

      headers = {
          'Total-Count': str(await self.instark_informer.count(
              'channel', domain))
      }

      return web.Response(headers=headers)

    #def get(self) -> Tuple[str, int]:
    async def get(self, request: web.Request):

      domain, limit, offset = get_request_filter(request)

      channels = ChannelSchema().dump(
          await self.instark_informer.search(
              'channel',domain, limit=limit, offset=offset), many=True)

      #return jsonify(channels)
      return web.json_response(channels, dumps=dumps)

    #def post(self) -> Tuple[str, int]:
    async def post(self, request: web.Request):

      data = ChannelSchema().loads( await request.data)

      channel = await self.subscription_coordinator.create_channel(data)

      #return json_channel, 201
      return web.Response(status=201)
