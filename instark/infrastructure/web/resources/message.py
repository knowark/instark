from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import MessageSchema
from ..helpers import get_request_filter


class MessageResource:
    def __init__(self, resolver: Injectark) -> None:
        self.resolver = resolver
        self.notification_coordinator = self.resolver['NotificationCoordinator']
        self.instark_informer = self.resolver['InstarkInformer']

    async def head(self, request) -> int:
        """
        ---
        summary: Return messages HEAD headers.
        tags:
          - Messages
        """
        domain, _, _ = await get_request_filter(request)

        headers = {
            'Total-Count': str(await self.instark_informer.count(
                'message', domain))
        }

        return web.Response(headers=headers)

    async def get(self, request: web.Request):
        """
        ---
        summary: Return all message.
        tags:
          - Messages
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Message'
        """
        domain, limit, offset = await get_request_filter(request)

        messages = MessageSchema().dump(
            await self.instark_informer.search(
                'message', domain, limit=limit,
                offset=offset), many=True)

        return web.json_response(messages, dumps=dumps)

    async def put(self, request: web.Request):
        """
        ---
        summary: Send message.
        tags:
          - Messages
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Message'
        responses:
          201:
            description: "Send message"
        """

        data = MessageSchema(
            many=True).loads(await request.text())

        message = await self.notification_coordinator.send_message(data)

        return web.Response(status=201)

    async def delete(self, request: web.Request):
        """
        ---
        summary: Delete message.
        tags:
          - Messages
        responses:
          204:
            description: "Message deleted."
        """
        ids = []
        uri_id = request.match_info.get('id')
        if uri_id:
            ids.append(uri_id)

        body = await request.text()
        if body:
            ids.extend(loads(await request.text()))

        result = await self.notification_coordinator.delete_message(ids)

        return web.Response(status=204)
