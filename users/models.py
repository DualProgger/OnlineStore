from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Модель пользователя интернет-магазина
"""
class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
