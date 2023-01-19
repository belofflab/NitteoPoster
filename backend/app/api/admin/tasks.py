from aiogram import Bot


BOT_TOKEN = ''
CHAT_ID = ''

bot = Bot(token='token')




async def send_message(text: str):
  return await bot.send_message(chat_id=CHAT_ID, text=text)