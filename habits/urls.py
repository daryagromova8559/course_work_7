from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitList, HabitCreate, HabitRetrieve, HabitUpdate, HabitDelete, PublicHabitsAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitList.as_view(),name='habit_list'),
    path('habit/create/', HabitCreate.as_view(),name='habit_create'),
    path('habit/<int:pk>', HabitRetrieve.as_view(),name='habit_get'),
    path('habit/update/<int:pk>', HabitUpdate.as_view(),name='habit_update'),
    path('habit/delete/<int:pk>', HabitDelete.as_view(),name='habit_delete'),
    path('habit/public/', PublicHabitsAPIView.as_view(), name='public_habits')
]
