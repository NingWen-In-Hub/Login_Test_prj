from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Profile


class LogInTestCase(TestCase):
    def setUp(self):
        self.password = 'AAAA123456'
        self.test_user = get_user_model().objects.create_user(
            username='blackcat',
            email='blackcat@white.com',
            password=self.password
        )

        self.client.login(email=self.test_user.email,
                          password=self.password)


class TestProfileCreateView(LogInTestCase):
    def test_create_profile_success(self):
        params = {'names': '名前',
                  'age': '862',
                  'photo': ''
                  }
        response = self.client.post(reverse_lazy('login_test_app:profile_create'), params)

        self.assertRedirects(response, reverse_lazy('login_test_app:profile_create'))
        self.assertEqual(Profile.objects.fliter(names='名前').count(), 1)
        
