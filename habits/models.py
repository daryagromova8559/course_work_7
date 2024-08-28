from django.db import models

from config import settings


class Habits(models.Model):
    sign_variants = (
        (True, 'Полезная'),
        (False, 'Вредная'),
    )

    period_variants = (
        ('everyday', 'Ежедневно'),
        ('every_week', 'Еженедельно'),
    )
    publish_variants = (
        (True, 'Опубликовано'),
        (False, 'Не опубликовано'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='Пользователь')
    place = models.CharField(max_length=50, blank=True, null=True, verbose_name='Место, в котором необходимо '
                                                                                'выполнять привычку.')
    time = models.TimeField(max_length=25, verbose_name='Время, когда надо выполнить привычку')
    action = models.CharField(max_length=100, blank=True, null=True, verbose_name='Действие, которое представляет '
                                                                                  'собой привычка.')
    sign_habit = models.BooleanField(choices=sign_variants, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name='Связанная с другой привычкой')

    periodicity = models.CharField(max_length=80, choices=period_variants, default='everyday',
                                   verbose_name='Периодичность')

    reward = models.CharField(max_length=100, blank=True, null=True, verbose_name='Вознаграждение')

    time_completed = models.SmallIntegerField(verbose_name='Время на выполнение')

    is_publish = models.BooleanField(choices=publish_variants, default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-id']
