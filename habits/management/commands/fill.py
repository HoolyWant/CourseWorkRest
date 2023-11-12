import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import BASE_DIR
from habits.models import Habits, Logs
from users.models import User

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):

    def handle(self, *args, **options):
        Logs.objects.all().delete()
        Habits.objects.all().delete()
        User.objects.all().delete()
        users_list = [
            {'email': 'sky@yandex.ru', 'tg_chat_id': '556203575',
             'tg_username': os.getenv('TG_USERNAME1')},
            {'email': 'sky@gmail.com', 'tg_chat_id': '650147568',
             'tg_username': os.getenv('TG_USERNAME2')},

        ]
        user_ids = []
        for user in users_list:
            new_user = User.objects.create(**user)
            new_user.set_password('qwerty')
            user_ids.append(new_user.id)

        pleasant_habit = Habits.objects.create(owner=User.objects.get(
                              pk=user_ids[0]),
                              time='16:20',
                              is_pleasant=True,
                              linked=None,
                              action='Съесть яблоко',
                              period='3',
                              is_public=True
                              )

        habits_list = [
            {'owner': user_ids[0], 'location': 'Дом',
             'time': '08:00', 'action': 'Зарядка',
             'is_pleasant': 'False', 'linked': pleasant_habit.id,
             'reward': None, 'period': 'daily',
             'limit': 60, 'is_public': 'False'},
            {'owner': user_ids[1], 'location': 'Дом',
             'time': '18:00', 'action': 'Прочитать 1 страницу',
             'is_pleasant': 'False', 'linked': None,
             'period': '4', 'reward': 'Съесть конфету',
             'limit': 60, 'is_public': 'False'},

        ]

        for habit in habits_list:
            if habit['linked'] is None:
                linked = None
            else:
                linked = Habits.objects.get(pk=habit['linked'])

            Habits.objects.create(owner=User.objects.get(pk=habit['owner']),
                                  location=habit['location'],
                                  time=habit['time'],
                                  is_pleasant=habit['is_pleasant'],
                                  linked=linked,
                                  action=habit['action'],
                                  period=habit['period'],
                                  reward=habit['reward'],
                                  limit=habit['limit'],
                                  is_public=habit['is_public']
                                  )
