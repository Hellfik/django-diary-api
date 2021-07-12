from django.test import TestCase
from base.models import Text
from django.contrib.auth.models import User

##########################
#      TEXT TESTS        #
##########################

class TextTestCase(TestCase):
    def setUp(self):
        """
           Set up function that creates fixtures, 
           here we create two users and a text associated
        """
        user1 = User.objects.create(email="test1.email@gmail.com", username="test1")
        user2 = User.objects.create(email="test2.email@gmail.com", username="test2")
        Text.objects.create(text='Test1 testing', client=user1)
        Text.objects.create(text='Test2 testing', client=user2)

    def test_text_str(self):
        """Test if the client associated with the text is the right one"""
        text1 = Text.objects.get(text="Test1 testing")
        text2 = Text.objects.get(text="Test2 testing")

        self.assertEqual(text1.client.username, 'test1')
        self.assertEqual(text2.client.username, 'test2')


##########################
#      USER TESTS        #
##########################

class UserTestCase(TestCase):
    def setUp(self):
        """
            Set up function that creates a user
        """
        User.objects.create(email="test1.email@gmail.com", username="test1")

    def test_user_create(self):
        """
        Check if the user has been added to the database
        """
        assert User.objects.count() == 1

