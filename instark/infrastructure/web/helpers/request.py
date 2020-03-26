from typing import Tuple, List, Dict, Any
from aiohttp import web
from .format import parse_domain, parse_dict
#from json import loads, decoder
#from flask import Request


def get_request_filter(request: web.Request) -> Tuple:
    filter = request.query.get('filter')
    limit = int(request.query.get('limit') or 1000)
    offset = int(request.query.get('offset') or 0)

    domain = parse_domain(filter)

    """if filter:
        try:
            domain = loads(filter)
        except decoder.JSONDecodeError:
            pass  """

    return domain, limit, offset


def get_parameters(request: web.Request) -> Dict[str, Any]:
    return parse_dict(request.query)
