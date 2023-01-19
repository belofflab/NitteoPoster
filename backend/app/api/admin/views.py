import decimal
import json
from bs4 import BeautifulSoup
from aiohttp import web

from app.api.admin.tasks import send_message

async def public_proceed_item(request: web.Request):
    print(await request.json())
    await send_message(text=str(await request.json()))
    return web.Response(text=json.dumps({'req': await request.json()}))


async def public_send_message(request: web.Request):
    data = await request.json()
    soup = BeautifulSoup(data['name'], 'lxml')

    block = soup.select('div.stepblock')
    block_lk = soup.select_one('div.stepblock.lichdann')

    text = f"""
    {block[0].select_one('div.steptitle').text}
    {block[0].select_one('div.stepblleft').text}
    {block[1].select_one('div.steptitle').text}
    {block[1].select_one('div.stepblleft').text}
    {block_lk.text}
    """
    await send_message(text=text)
    return web.Response(text=json.dumps({'req': await request.json()}))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
