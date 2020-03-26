from injectark import Injectark
from aiohttp import web
from aiohttp_jinja2 import render_template
from .... import __version__
from .message import MessageResource
from .channel import ChannelResource
from .device import DeviceResource
from .subscription import SubscriptionResource


class RootResource():

    def __init__(self, spec) -> None:
        self.spec = spec

    async def get(self) -> str:
        if 'api' in request.args:
            return web.json_response(self.spec.to_dict())

        """template = render_template(
            'index.html', url="/?api", version=__version__)
        response = make_response(template, 200, {
            'Content-Type': 'text/html'
        })"""

        context = {'url': '/?api', 'version': __version__}
        response = render_template(
            'index.html', request, context)
        response.headers['Content-Type'] = 'text/html'
        
        return response
