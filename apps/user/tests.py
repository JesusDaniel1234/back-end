from tests.test_setup import TestSetUp
from rest_framework import status

from apps.user.models import UserProfile


# Create your tests here.
class TestUser(TestSetUp):
    URL = "http://localhost:8000/api/v2/user/"

    def test_list_users_by_url(self):
        response = self.client.get(self.URL, format="json")

        # Al hacer las migraciones debe crearse automaticamente un superusuario
        # Y El TestSetUp crea un superusuario por defecto, entonces deben hacer 2 usuarios
        self.assertEqual(len(response.data), 2)

    def test_create_user_by_url(self):
        data = {
            "username": "JesusDaniel",
            "first_name": "Jesús Daniel",
            "last_name": "Sánchez Alarcón",
            "email": "jesus@gmail.com",
            "password": "testuser1234"
        }

        response = self.client.post(self.URL, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["user"]["username"], data["username"])

    def test_update_user_by_url(self):
        user = UserProfile.objects.create(username="User", email="email@user.com", password="password")

        data = {
            "first_name": "Jesús Daniel",
            "last_name": "Sánchez Alarcón",
            "email": "jesus@gmail.com"
        }

        response = self.client.patch(f"{self.URL}{user.id}/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["email"], data["email"])

    def test_detele_user_by_url(self):
        user = UserProfile.objects.create(username="User", email="email@user.com", password="password")

        response = self.client.delete(f"{self.URL}{user.id}/", format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
