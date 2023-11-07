from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    ONE_DAY_PER_WEEK = '1'
    TWO_DAYS_PER_WEEK = '2'
    TREE_DAYS_PER_WEEK = '3'
    FOUR_DAYS_PER_WEEK = '4'
    FIVE_DAYS_PER_WEEK = '5'
    SIX_DAYS_PER_WEEK = '6'
    DAILY = 'daily'

    PERIODS = (
        (ONE_DAY_PER_WEEK, 'один день в неделю'),
        (TWO_DAYS_PER_WEEK, 'два дня в неделю'),
        (TREE_DAYS_PER_WEEK, 'три дня в неделю'),
        (FOUR_DAYS_PER_WEEK, 'четыре дня в неделю'),
        (FIVE_DAYS_PER_WEEK, 'пять дней в неделю'),
        (SIX_DAYS_PER_WEEK, 'шесть дней в неделю'),
        (DAILY, 'ежедневно'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE, related_name='habits')
    location = models.CharField(max_length=100, default='где угодно', verbose_name='место выполнения')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=500, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    linked = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    period = models.CharField(max_length=20, choices=PERIODS, default=DAILY, verbose_name='периодичность привычки')
    reward = models.CharField(max_length=500, verbose_name='награда за выполнение')
    limit = models.IntegerField(default=60, verbose_name='время на выполнение'),
    is_public = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


class Logs(models.Model):
    habit = models.ForeignKey(Habits, on_delete=models.CASCADE, verbose_name='привычка', **NULLABLE)
    last_attempt = models.DateTimeField(verbose_name='последняя отправка')