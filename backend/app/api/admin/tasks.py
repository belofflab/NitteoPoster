from aiogram import Bot

from data.config import BOT_TOKEN, CHAT_ID
print(BOT_TOKEN, CHAT_ID)
bot = Bot(token=BOT_TOKEN)


async def send_message(text: str):
  return await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='HTML')


