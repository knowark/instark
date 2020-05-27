from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import SubscriptionSchema
from ..helpers import get_request_filter


class SubscriptionResource:

    def __init__(self, resolver: Injectark) -> None:
        self.resolver = resolver
        self.subscription_coordinator = self.resolver['SubscriptionCoordinator']
        self.instark_informer = self.resolver['InstarkInformer']

    async def head(self, request) -> int:
        """
        ---
        summary: Return subscriptions HEAD headers.
        tags:
          - Subscriptions
        """
        domain, _, _ = await get_request_filter(request)

        headers = {
            'Total-Count': str(await self.instark_informer.count(
                'subscription', domain))
        }

        return web.Response(headers=headers)

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

        domain, limit, offset = await get_request_filter(request)

        subscriptions = SubscriptionSchema().dump(
            await self.instark_informer.search(
                'subscription', domain, limit=limit,
                offset=offset), many=True)

        return web.json_response(subscriptions, dumps=dumps)

    async def put(self, request: web.Request):
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

        data = SubscriptionSchema(many=True).loads(await request.text())

        subscription = await self.subscription_coordinator.subscribe(data)

        return web.Response(status=201)

    async def delete(self, request: web.Request):
        """
        ---
        summary: Delete Subscription.
        tags:
          - Subscriptions
        responses:
          204:
            description: "Subscription deleted."
        """
        ids = []
        uri_id = request.match_info.get('id')
        if uri_id:
            ids.append(uri_id)

        body = await request.text()
        if body:
            ids.extend(loads(await request.text()))

        result = await self.subscription_coordinator.delete_subscribe(ids)

        return web.Response(status=204)
