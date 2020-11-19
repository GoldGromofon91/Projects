from django.test import TestCase
from django.test import Client

from .models import User

# Create your tests here.
class URLTests(TestCase): 
    fixtures = ['initial_data.json']
    def test_post_user(self):
        response = self.client.post('/api/v1/users/',             
        {   'username':'test_name1',
                'username': 'Test_post',
                'is_active':True,
                'password':'asdasdasdasd',
                'first_name':'Hello_post',
                'last_name':'last_post'
            },
            content_type='application/json').json()

        self.assertEqual(response['username'], 'Test_post')
        self.assertEqual(response['is_active'], True)  
        # self.assertEqual(response['password'], 'asdasdasdasd') 
        self.assertEqual(response['first_name'], 'Hello_post') 
        self.assertEqual(response['last_name'], 'last_post')

        user = User.objects.get(id = response['id'])
        
        self.assertEqual(user.username, 'Test_post')
        self.assertEqual(user.is_active, True)
        # self.assertEqual(user.password, 'asdasdasdasd')
        self.assertEqual(user.first_name, 'Hello_post')
        self.assertEqual(user.last_name, 'last_post')

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
                'is_active':False,
                'first_name':'hello'
            },
            content_type='application/json').json()
        self.assertEqual(response['first_name'], 'hello')
        
    
    def test_patch_method(self):
        response = self.client.patch('/api/v1/users/7', 
            {  
                'first_name':'Leo'
            },
            content_type='application/json').json()
        self.assertEqual(response['first_name'], 'Leo')

    def test_delete_method(self):
        response = self.client.delete('/api/v1/users/7')
        user = User.objects.filter(pk=7)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(user), 0)

    def test_get_token(self):

        response = self.client.post('/api-token-auth/', {'username':'user3','password':'hello'},
        content_type='application/json')

        self.assertEqual(response.status_code,200)

    def test_get_token_wrong_password(self):
        response = self.client.post('/api-token-auth/', {'username':'user3','password':'hello1'},
        content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_get_token_unregister_user(self):
        response = self.client.post('/api-token-auth/', {'username':'user234234','password':'hello'},
        content_type='application/json')
        
        self.assertEqual(response.status_code,401)