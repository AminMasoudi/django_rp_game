from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from main.models import Roles

# Create your tests here.

class UsersTestCase(TestCase):

    def setUp(self) -> None:
        self.username = "test"
        self.password = "whatch0ut"
        r = Roles.objects.create()
        a = UserProfile.objects.create_user(username=self.username, password=self.password, role=r)

    def test_a(self):
        c = Client()
        post_response = c.post(reverse("user:login"), {"username": self.username,
                                                             "password": self.password})
    def test_signup(self):
        c = Client()
        post_response = c.post(username="qwerty", password="qwerty7410@")
        