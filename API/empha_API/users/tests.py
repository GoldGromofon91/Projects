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

    def test_get_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_individual_users(self):
        response = self.client.get('/api/v1/users/7') 
        self.assertEqual(response.json()['id'], 7)

    def test_put_method(self):
        user = User.objects.get(id=7)
        response = self.client.put('/api/v1/users/7', 
            {   'username':'test_name1',
                'password':'asdasdasd',
                'is_active':'False',
                'first_name':'asdasdasdasdasdqwe'
            },
            content_type='application/json').json()

        self.assertNotEqual(user.first_name,response['first_name'])
    
    def test_patch_method(self):
        response = self.client.put('/api/v1/users/7', 
            {  
                'password':'asdasdasd',
                'is_active':'False',
                'first_name':'qzxczxcsdqwe'
            },
            content_type='application/json').json()
        self.assertEqual(response['username'], ['This field is required.'])

    def test_delete_method(self):
        response = self.client.delete('/api/v1/users/7')
        self.assertEqual(response.status_code, 204)
