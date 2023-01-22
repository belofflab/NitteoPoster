import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__name__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if os.path.exists(ENV_FILE):
    load_dotenv(ENV_FILE)


SECRET_KEY = os.getenv('SECRET_KEY')

BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMISSIONS = int(os.getenv('COMMISSIONS')) 
OERDERS = int(os.getenv('OERDERS'))
CHANGE_OWN_COMMISSION = int(os.getenv('CHANGE_OWN_COMMISSION'))
