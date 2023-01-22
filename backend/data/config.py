import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__name__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if os.path.exists(ENV_FILE):
    load_dotenv(ENV_FILE)


SECRET_KEY = os.getenv('SECRET_KEY')

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = int(os.getenv('CHAT_ID')) # -1001714792398

