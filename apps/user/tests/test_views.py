from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.shortcuts import reverse
from apps.user import views
from mixer.backend.django import mixer


class TestLoginView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse("login")
        self.email = "cosme@fulanito.com"
        self.password = "Me da una copilla porfavor"
        self.data = {"email": self.email, "password": self.password}

    def test_request_no_data(self):
        request = self.factory.post(self.url)
        response = views.LoginView.as_view()(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, {"error": "Please provide both username and password"}
        )

    def test_request_non_existant_user(self):
        request = self.factory.post(self.url, data=self.data)
        response = views.LoginView.as_view()(request)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"error": "Invalid Credentials"})

    def test_valid_login(self):
        user = mixer.blend("user.User", username=self.email, email=self.email)
        user.set_password(self.password)
        user.save()
        request = self.factory.post(self.url, data=self.data)
        response = views.LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
        self.assertIsNotNone(response.data["token"])
