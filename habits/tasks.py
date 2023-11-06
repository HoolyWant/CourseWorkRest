from datetime import datetime, timedelta

from celery import shared_task
from dateutil.relativedelta import relativedelta

from habits.models import Habits, Logs
from habits.telegram_bot import send_notify
from users.models import User


@shared_task
def telegram_habit_mailling() -> None:
    habits = Habits.objects.all()
    logs = Logs.objects.all()
    weekends = [6, 7]
    for habit in habits:
        last_attempt = logs.filter(habit=habit.id).last().last_attempt
        if habit.time == datetime.now().time():
            if not logs.filter(habit=habit.id).last().last_attempt and habit.period == 'daily':
                send_notify(habit)
            elif habit.period == '1' and datetime.now() == (last_attempt + timedelta(days=7)):
                send_notify(habit)
            elif habit.period == '2' and datetime.now() == (last_attempt + timedelta(days=4)):
                send_notify(habit)
            elif habit.period == '3' and datetime.now() == (last_attempt + timedelta(days=3)):
                send_notify(habit)
            elif habit.period == '4' and datetime.now() == (last_attempt + timedelta(days=2)):
                send_notify(habit)
            elif habit.period == '5' and datetime.today().weekday() not in weekends:
                send_notify(habit)
            elif habit.period == '6' and datetime.today().weekday() not in weekends[1]:
                send_notify(habit)








