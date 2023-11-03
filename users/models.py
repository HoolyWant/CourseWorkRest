from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    tg_chat_id = models.CharField(max_length=100, unique=True, verbose_name='tg_chat_id')
    tg_username = models.CharField(max_length=100, unique=True, verbose_name='tg_username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.tg_username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
