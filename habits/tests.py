from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    """ Тестирование модели Habits """

    def setUp(self):
        """ Создание тестовой модели Пользователя (с авторизацией) и Привычки """

        self.user = User.objects.create(
            email="test@test.com",
            password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place="Дома",
            time="07:00:00",
            action="Утренняя зарядка",
            time_completed=15,
            sign_habit=True,
            periodicity='everyday',
            is_publish=True,
        )

    def test_create_habit(self):
        """ Тестирование создания привычки """

        url = reverse("habits:habit_create")
        data = {
            "user": self.user.pk,
            "place": "Дома",
            "time": "07:00:00",
            "action": "Утренняя зарядка",
            "time_completed": 15,
            "sign_habit": True,
            "periodicity": 'everyday',
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'id': 2, 'place': 'Дома', 'time': '07:00:00', 'action': 'Утренняя зарядка',
                                           'sign_habit': True, 'periodicity': 'everyday', 'reward': None,
                                           'time_completed': 15,
                                           'is_publish': False, 'user': 1, 'related_habit': None})

    def test_list_habit(self):
        """ Тестирование вывода всех привычек """

        response = self.client.get(reverse('habits:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """ Тестирование просмотра одной привычки """

        url = reverse("habits:habit_get", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 6, 'place': 'Дома', 'time': '07:00:00', 'action': 'Утренняя зарядка',
                                           'sign_habit': True, 'periodicity': 'everyday', 'reward': None,
                                           'time_completed': 15,
                                           'is_publish': True, 'user': 5, 'related_habit': None})

    def test_update_habit(self):
        """ Тестирование изменений привычки """

        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Улица",
            "time": "07:30:00",
            "action": "ТПробежка",
            "time_completed": 60,
            "sign_habit": True,
            "periodicity": 'everyday',
        }
        response = self.client.put(url, data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 7, 'place': 'Улица', 'time': '07:30:00', 'action': 'ТПробежка', 'sign_habit': True,
                          'periodicity': 'everyday', 'reward': None, 'time_completed': 60, 'is_publish': True,
                          'user': 6, 'related_habit': None})

    def test_delete_habit(self):
        """ Тестирование удаления привычки """

        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_public_habit(self):
        """ Тестирование вывода публичных привычек """

        response = self.client.get(reverse('habits:public_habits'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)