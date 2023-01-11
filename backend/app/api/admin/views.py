import decimal
import json

from aiohttp import web

async def public_proceed_item(request: web.Request):
    print(request)
    return request

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
