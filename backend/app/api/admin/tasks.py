from aiogram import Bot


BOT_TOKEN = '5737422661:AAEtASYHz-12g7tpKlOH6-6nA0rc35A65Sc'
CHAT_ID = -1001714792398
CHANNEL_ID = -1001714792398

bot = Bot(token=BOT_TOKEN)




async def send_message(text: str):
  return await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='HTML')

async def send_shablon(text: str):
  return await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='HTML')