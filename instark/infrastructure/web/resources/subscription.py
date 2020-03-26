from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import SubscriptionSchema
from ..helpers import get_request_filter


class SubscriptionResource:

    def __init__(self, resolver: Injectark) -> None:
        self.resolver = resolver
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
                'subscription', domain))
        }

        return web.Response(headers=headers)

    #def get(self) -> Tuple[str, int]:
    async def get(self, request: web.Request):
        """
        ---
        summary: Return all subscriptions.
        tags:
          - Subscriptions
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Subscription'
        """
        
        domain, limit, offset = get_request_filter(request)

        subscriptions = SubscriptionSchema().dump(
            await self.instark_informer.search(
              'subscription',domain, limit=limit,
                offset=offset), many=True)

        #return jsonify(subscriptions)
        return web.json_response(subscriptions, dumps=dumps)

    
    #def post(self) -> Tuple[str, int]:
    async def post(self, request: web.Request):
        """
        ---
        summary: Register subscription.
        tags:
          - Subscriptions
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Subscription'
        responses:
          201:
            description: "Subscription created"
        """

        #data = SubscriptionSchema().loads(request.data or '{}')

        subscription = self.subscription_coordinator.subscribe(data)

        #return json_subscription, 201
        return web.Response(status=201)
  
    
      
    

    