from injectark import Injectark
from aiohttp import web
from rapidjson import dumps, loads
from ..schemas import MessageSchema
from ..helpers import get_request_filter


class MessageResource():

    def __init__(self, resolver: Injectark) -> None:
        #self.notification_coordinator = resolver['NotificationCoordinator']
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
        domain, limit, offset = get_request_filter(request)

        messages = MessageSchema().dump(
            await self.instark_informer.search(
              'message',domain,limit=limit,
                offset=offset), many=True)

        #return jsonify(messages)
        return web.json_response(messages, dumps=dumps)



    #def post(self) -> Tuple[str, int]:
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

        #data = MessageSchema().loads(request.data)
        data = MessageSchema(
            many=True).loads(await request.text())

        message = await self.notification_coordinator.send_message(data)

       # return json_message, 201
        return web.Response(status=200)

    
    
