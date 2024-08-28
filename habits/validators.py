from rest_framework import serializers


class HabitsValidation:
    """Валидатор на ссылку к видео"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['sign_habit']:
            if value['related_habit'] or value['reward']:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть связанной привычки или вознаграждения')
            if value['related_habit'] and value['reward']:
                raise serializers.ValidationError(
                    'Может быть связанная привычка или вознаграждение,')
            if value['time_completed'] > 2:
                raise serializers.ValidationError(
                    'Длительность привычки не может быть больше 2 минут')
            if value['related_habit']:
                if not value['related_habit'].sign_habit:
                    raise serializers.ValidationError('Связанные привычки = приятные привычки')
                if value['related_habit'].periodicity > 7:
                    raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')



