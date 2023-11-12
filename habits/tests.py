from rest_framework import status

from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsApiTestCAse(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='testuser@mail.ru', password='test', tg_chat_id='dd',
                                        tg_username='dd')
        self.client.force_authenticate(user=self.user)
        self.data = {
            "time": "10:05",
            "is_pleasant": True,
            "action": "Съесть грушу",
            "period": "4",
            "is_public": True,
            "limit": 60
            }
        self.patch_data = {
            "time": "12:05",
            "limit": 70,
            }

        self.model = Habits.objects.create(owner=self.user, time='12:12', action='test3', reward='test3', limit=60)

    def test_get(self):
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post('/habits/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        response = self.client.patch(f'/habits/{self.model.id}/', data=self.patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(f'/habits/{self.model.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_public(self):
        response = self.client.get('/habits/public/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
