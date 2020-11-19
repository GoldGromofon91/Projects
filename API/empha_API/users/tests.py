from django.test import TestCase
from django.test import Client

from .models import User

# Create your tests here.
class URLTests(TestCase): 
    fixtures = ['initial_data.json']
    
    def test_auth_username_label(self):
        user = User.objects.get(id=7)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_auth_is_superuser_value_label(self):
        user = User.objects.get(id=7)
        self.assertEquals(user.is_superuser,False)

    def test_auth_password_max_length(self):
        user = User.objects.get(id=7)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length,128)

    def test_get_users(self):
        response = self.client.get('/api/v1/users/') 
        self.assertEqual(response.status_code, 200)

    def test_get_individual_users(self):
        response = self.client.get('/api/v1/users/7') 
        self.assertEqual(response.json()['id'], 7)

    