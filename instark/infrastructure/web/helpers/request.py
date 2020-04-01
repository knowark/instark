from typing import Tuple, List, Dict, Any
from aiohttp import web
from .format import parse_domain


def get_request_filter(request: web.Request) -> Tuple:
    filter = request.query.get('filter')
    limit = int(request.query.get('limit') or 1000)
    offset = int(request.query.get('offset') or 0)

    domain = parse_domain(filter)

    return domain, limit, offset
