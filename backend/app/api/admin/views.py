import decimal
import json

from aiohttp import web

from app.api.admin.tasks import send_message

async def public_proceed_item(request: web.Request):
    print(await request.json())
    await send_message(text=str(await request.json()))
    return web.Response(text=json.dumps({'req': await request.json()}))


async def public_send_message(request: web.Request):
    # print(await request.json())
    await send_message(text="Отправили сообщение ")
    return web.Response(text=json.dumps({'req': 'await request.json()'}))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
