import decimal
import json
import xml.etree.ElementTree as ET

import requests
from aiohttp import web
from app.api.admin.manager import DBManager
from app.api.admin.tasks import send_message, send_shablon
from bs4 import BeautifulSoup
from data.config import BASE_DIR


async def make_shablon():
    db = DBManager()

    response = requests.get('http://gogo.exchange/request-exportxml.xml').text
    root = ET.fromstring(response)
    data_list = []
    for item in root.findall('item'):
        city = item.find('city')
        from_id = item.find('from')
        to_id = item.find('to')
        try:
            city = city.text
        except AttributeError:
            city = 0

        data_list.append({'city': city, 'from': from_id.text, 'to': to_id.text})
    # print(data_list)

    with open(f'{BASE_DIR}/media/cyties.json' ,'r', encoding='utf-8') as file:
        cities_codes = json.load(file)
    countries = {'Турция': [], 'Испания': [], 'Литва': [], 'Польша': [], 'Россия': []}
    for res_data_list in data_list:
        res_from = db.get_xml(xml_cod=res_data_list.get('from'))[0]
        res_to = db.get_xml(xml_cod=res_data_list.get('to'))[0]
        courses = db.get_course(res_from[0], res_to[0])[0]
        if float(courses[3]) != 1:
            course = courses[3]
        else:
            course = courses[4]
        if cities_codes.get(res_data_list.get("city")):
            countries[cities_codes.get(res_data_list.get("city")).split(', ')[1]].append({'city': cities_codes.get(res_data_list.get("city")).split(', ')[0], 'way': f'{res_from[1]} --> {res_to[1]}', 'course': course})
            # print(f'City: {cities_codes.get(res_data_list.get("city"))} · {res_from[1]} --> {res_to[1]} · {course}')
    text = ''
    for country in countries:
        text = text + f'\n<b>{country.upper()}</b>\n\n' 
        for data in countries[country]:
            text = text + f'{data.get("city")}: {data.get("way")} · курс <i>{data.get("course")}</i>\n'
    return text

async def public_proceed_item(request: web.Request):
    data = await request.json()
    await send_message(text=f"""
Изменение комиссии!

{data['title_pair_give']} -> {data['title_pair_get']}: {data['pair_give'].split(' ')[-1] if len(data['pair_give']) > 3 else data['pair_get'].split(' ')[-1]}%
    
""")
    return web.Response(text=json.dumps({'req': await request.json()}))

async def public_proceed_items(request: web.Request):
    data = await request.json()
    # manager = DBManager()
    # text = manager.get_all_napobmens()
    await send_shablon(text=await make_shablon())
    return web.Response(text=json.dumps({'req': await request.json()}))


async def public_send_message(request: web.Request):
    data = await request.json()
    print(data)
    soup = BeautifulSoup(data['name'], 'lxml')
    db = DBManager()
    block = soup.select('div.stepblock')
    block_lk = soup.select_one('div.stepblock.lichdann')

    text = f"""
    <b>Уведомелние с сайта</b>

    НОВАЯ ЗАЯВКА #<code>{db.get_last_order_id()}</code>
    {block[0].select_one('div.stepblleft').text}
    {block[1].select_one('div.steptitle').text}
    {block[1].select_one('div.stepblleft').text}
    {block_lk.text.replace('Имя:', 'Telegram:')}
    """
    print(text)
    await send_message(text=text)
    return web.Response(text=json.dumps({'req': await request.json()}))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
