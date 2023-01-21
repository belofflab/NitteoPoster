from aiogram import Bot


BOT_TOKEN = '5759038625:AAGeKrBxcT-_fLUa4-D3yx22dhP2Ik6ZOv8'
CHAT_ID = -883474105

bot = Bot(token=BOT_TOKEN)




async def send_message(text: str):
  return await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='HTML')