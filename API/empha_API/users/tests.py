from django.test import TestCase
from django.test import Client

from .models import User
import base64

class URLTests(TestCase): 
    fixtures = ['initial_data.json']
    def test_post_user(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.post('/api/v1/users/',             
        {   
                'username': 'Test_post',
                'is_active': True,
                'password': 'qweQWE123',
                'first_name': 'Hello_post',
                'last_name': 'last_post'
            },
            content_type='application/json', **header).json()
        
        self.assertEqual(response['username'], 'Test_post')
        self.assertEqual(response['is_active'], True)  
        self.assertEqual(response['password'], 'pbkdf2_sha256$216000$Test_post$T5aD7YMUwHokOQyxZGaV4sk/tTHSEWUC0IcfCl+GXQ0=') 
        self.assertEqual(response['first_name'], 'Hello_post') 
        self.assertEqual(response['last_name'], 'last_post')

        user = User.objects.get(id = response['id'])
        
        self.assertEqual(user.username, 'Test_post')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.password, 'pbkdf2_sha256$216000$Test_post$T5aD7YMUwHokOQyxZGaV4sk/tTHSEWUC0IcfCl+GXQ0=')
        self.assertEqual(user.first_name, 'Hello_post')
        self.assertEqual(user.last_name, 'last_post')

    def test_get_all_users(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.get('/api/v1/users/', ** header)
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.json()['id'], 4)

    def test_put_method(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        user = User.objects.get(id=4)
        response = self.client.put('/api/v1/users/4', 
            {   
                'username': 'user_2_post',
                'password': 'qweQWE123',
                'is_active': True,
                'first_name': 'Test',
                'last_name' : 'Test'
            },
            content_type='application/json', **header).json()
        self.assertEqual(response['first_name'], 'Test')
        
    
    def test_patch_method(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.patch('/api/v1/users/4', 
            {  
                'first_name': 'Leo'
            },
            content_type='application/json', ** header).json()
        self.assertEqual(response['first_name'], 'Leo')

    def test_delete_method(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.delete('/api/v1/users/4',**header)
        user = User.objects.filter(pk=7)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(user), 0)

    def test_get_token(self):
        response = self.client.post('/api-token-auth/', {'username':'user_2_post','password':'qweQWE123'},
        content_type='application/json')

        self.assertEqual(response.status_code,200)

    def test_get_token_wrong_password(self):
        response = self.client.post('/api-token-auth/', {'username':'user_2_post','password':'hello1'},
        content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_get_token_unregister_user(self):
        response = self.client.post('/api-token-auth/', {'username':'user234234','password':'hello'},
        content_type='application/json')
        
        self.assertEqual(response.status_code,401)

    def test_incorrect_header(self):
        header = {
            'HTTP_USERNAME': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.status_code,403)
    
    def test_empty_header(self):
        header = {
            'HTTP_': 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.status_code,403)

    def test_incorrect_len_header_values(self):
        header = {
            'HTTP_Authorization': " " + 'Token ' + 'f965bf7efadd45d88557e711497b477d',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.status_code,403)

    def test_incoret_hash(self):
        header = {
            'HTTP_Authorization': 'Token ' + 'f965bf7efadd45d88557e711497b4734',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.status_code,403)
    
    def test_incorect_type_auth(self):
        header = {
            'HTTP_Authorization': 'Basic ' + 'f965bf7efadd45d88557e711497b4734',
        }
        response = self.client.get('/api/v1/users/4', **header) 
        self.assertEqual(response.status_code,403)