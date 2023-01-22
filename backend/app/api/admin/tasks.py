from aiogram import Bot

from data.config import BOT_TOKEN, COMMISSIONS, OERDERS, CHANGE_OWN_COMMISSION

bot = Bot(token=BOT_TOKEN)



async def send_message_shablon(text: str):
  return await bot.send_message(chat_id=OERDERS, text=text, parse_mode='HTML')

async def send_message_orders(text: str):
  return await bot.send_message(chat_id=OERDERS, text=text, parse_mode='HTML')

async def send_message_own_com(text: str):
  return await bot.send_message(chat_id=CHANGE_OWN_COMMISSION, text=text, parse_mode='HTML')


