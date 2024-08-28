from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time', 'action', 'sign_habit', 'related_habit', 'periodicity', 'reward',
                    'time_completed', 'is_publish')
    list_filter = ('user',)
    search_fields = ('user',)

