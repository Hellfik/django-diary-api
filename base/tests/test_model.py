from django.test import TestCase
from base.models import Text

class TestAppModels(TestCase):

    def test_model_str(self):
        text = Text.objects.create(text='Test testing')
        self.assertEqual(str(text), 'Test testing')
