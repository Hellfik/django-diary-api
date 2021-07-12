from django.test import TestCase
from base.models import Text
from django.contrib.auth.models import User

class UserListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 2 users
        user1 = User.objects.create(email="test1.email@gmail.com", username="test1")
        user2 = User.objects.create(email="test2.email@gmail.com", username="test2")
        # Create 1 text for each user
        Text.objects.create(text="Test1", client=user1)
        Text.objects.create(text="Test2", client=user2)

    def test_view_url_exists_at_desired_location_api(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_front(self):
        user1 = User.objects.get(id=1)
        id_user = user1.id
        response = self.client.get(f'/protected/user/{id_user}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'protected/profile_admin.html')
