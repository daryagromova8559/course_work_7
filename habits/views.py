from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer


class HabitCreate(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.user = self.request.user
        new_habits.save()


class HabitList(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieve(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdate(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()


class HabitDelete(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitsAPIView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_publish=True)
    serializer_class = HabitsSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitsPagination
