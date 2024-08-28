from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='users/photo', verbose_name='Аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True,
                             null=True, help_text='Введите номер телефона')

    city = models.CharField(max_length=35, verbose_name='Город', blank=True,
                            null=True, help_text='Введите город')

    tg_chat_id = models.CharField(max_length=55, blank=True, null=True, verbose_name='Телеграмм id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
