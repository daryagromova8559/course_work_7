from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import User
from users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDelete(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
