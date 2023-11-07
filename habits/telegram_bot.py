import os
from datetime import datetime

import telebot
from dotenv import load_dotenv
from config.settings import BASE_DIR

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

bot = telebot.TeleBot(os.getenv('TELEBOT_API_KEY'))


def send_notify(habit):
    chat_id = habit.owner.__dict__['chat_id']
    if habit.is_pleasant:
        bot.send_message(chat_id=chat_id, text=f'Наступило время {habit.action}! '
                                                f'Если вы находитесь {habit.location}, у вас есть {habit.limit},'
                                                f'чтобы выполнить эту привычку!'
                                                f'Это приятная привычка, поэтому вознаграждение '
                                                f'вы за нее не получите)')
    elif habit.linked is not None:
        bot.send_message(chat_id=chat_id, text= f'Наступило время {habit.action}! '
                                                f'Если вы находитесь {habit.location}, у вас есть {habit.limit},'
                                                f'чтобы выполнить эту привычку!'
                                                f'После выполнения в виде аознаграждения '
                                                f'вы можете {habit.linked.__dict__["action"]}')
    else:
        bot.send_message(chat_id=chat_id, text=f'Наступило время {habit.action}! '
                                                f'Если вы находитесь {habit.location}, у вас есть {habit.limit},'
                                                f'чтобы выполнить эту привычку!'
                                                f'После выполнения в виде аознаграждения'
                                                f'вы можете {habit.reward}')
