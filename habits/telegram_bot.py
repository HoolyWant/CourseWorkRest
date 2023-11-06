import os

import telebot
from dotenv import load_dotenv
from config.settings import BASE_DIR

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

bot = telebot.Telebot(os.getenv('TELEBOT_API_KEY'))

