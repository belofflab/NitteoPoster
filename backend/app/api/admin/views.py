import decimal
import json
from bs4 import BeautifulSoup
from aiohttp import web

from app.api.admin.tasks import send_message
from app.api.admin.manager import DBManager

async def public_proceed_item(request: web.Request):
    data = await request.json()
    await send_message(text=f"""
Изменение комиссии!

{data['title_pair_give']} -> {data['title_pair_get']}: {data['pair_give'].split(' ')[-1] if len(data['pair_give']) > 3 else data['pair_get'].split(' ')[-1]}%
    
""")
    return web.Response(text=json.dumps({'req': await request.json()}))

async def public_proceed_items(request: web.Request):
    data = await request.json()
    manager = DBManager()
    text = manager.get_all_napobmens()
    await send_message(text=text)
    return web.Response(text=json.dumps({'req': await request.json()}))


async def public_send_message(request: web.Request):
    data = await request.json()
    soup = BeautifulSoup(data['name'], 'lxml')

    block = soup.select('div.stepblock')
    block_lk = soup.select_one('div.stepblock.lichdann')
    # print(f"1. {block[0].select_one('div.stepblleft').text}\n2. {block[1].select_one('div.steptitle').text.replace('Получаете', 'Получаете')}\n3. {block[1].select_one('div.stepblleft').text}\n{block_lk.text.replace('Имя:', 'Telegram:')}")

    text = f"""
    Уведомелние с сайта

    {block[0].select_one('div.stepblleft').text}
    {block[1].select_one('div.steptitle').text.replace('Получаете', 'ТЕСТИМ')}
    {block[1].select_one('div.stepblleft').text}
    {block_lk.text.replace('Имя:', 'Telegram:')}
    """
    await send_message(text=text)
    return web.Response(text=json.dumps({'req': await request.json()}))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
