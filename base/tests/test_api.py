from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Text
from django.contrib.auth.models import User


class UserTests(APITestCase):
    def setUp(self) -> None:
        """
        Set up the user for the api test cases
        """
        self.user = User.objects.create(
            username="Test",
            email="test.email@gmail.com"
        )

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/users/'
        response = self.client.post(url, self.user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_delete_user(self):
        """
        Ensure we can delete a user object.
        """
        count_user_before = User.objects.count()
        url = f'/api/users/{self.user.id}'
        response = self.client.delete(url)
        self.assertEqual(User.objects.count(), count_user_before)

    def test_update_user(self):
        """
        Ensure we can create a new user object.
        """
        url = f'api/users/{self.user.id}'
        data = {
            'username' : "Test_update",
            'email' : 'test.email@gmail.com'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(self.user.username, "Test_update")