from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        from user.models import UserProfile

        self.login_url = "/api/v1/token/"
        self.user = UserProfile.objects.create_superuser(
            username="superuser",
            email="superuser@admin.com",
            password="admin1234",
            first_name="develop",
            last_name="develop",
            phone_number="55075002"
        )

        response = self.client.post(self.login_url, {
            "username": self.user.username,
            "password": "admin1234"
        }, format="json")

        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        return super().setUp()
