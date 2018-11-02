from django.test import TestCase
from .models import ProfileToken
from rest_framework.test import APITestCase

# Create your tests here.
class SaveUserTokenTest(APITestCase):
    def test_without_params(self):
        #Checking POST without any
        profile = {'test': 'test'}
        response = self.client.post('/api/save_user_token/', profile)
        self.assertEqual(response.status_code, 400)

        #Checking POST with user_id and no user_token
        profile = {'user_id': '1'}
        response = self.client.post('/api/save_user_token/', profile)
        self.assertEqual(response.status_code, 400)

        #Checking POST with user_token and no user_id
        profile = {'user_token': 'ThisIsAToken'}
        response = self.client.post('/api/save_user_token/', profile)
        self.assertEqual(response.status_code, 400)

    def test_new_profile(self):
        #Checking CREATE new profile token
        profile = {'user_token': 'ThisIsAToken', 'user_id': '1'}
        response = self.client.post('/api/save_user_token/', profile)
        self.assertEqual(response.status_code, 200)

        profile = {'user_token': 'OtherToken', 'user_id': '2'}
        response = self.client.post('/api/save_user_token/', profile)

        profile1 = ProfileToken.objects.all()[0]
        profile2 = ProfileToken.objects.all()[1]

        self.assertEqual(profile1.user_token, 'ThisIsAToken')
        self.assertEqual(profile1.user_id, 1)

        self.assertEqual(profile2.user_token, 'OtherToken')
        self.assertEqual(profile2.user_id, 2)

    def test_update_profile(self):
        #Create a profile to update
        ProfileToken.objects.create(
                            user_token = 'ThisIsAToken',
                            user_id = 1)

        #Checking UPDATE existing profile
        profile = {'user_token': 'ThisISOtherToken', 'user_id': '1'}
        response = self.client.post('/api/save_user_token/', profile)
        self.assertEqual(response.status_code, 200)

        profile1 = ProfileToken.objects.all()[0]
        self.assertEqual(profile1.user_token, 'ThisISOtherToken')

class SendPushMessageTest(APITestCase):
    def test_invalid_token_push(self):
        ProfileToken.objects.create(
            user_id = 1,
            user_token = 'notValidToken')

        request = {'user_id': '1', 'title': 'ThisIsATitle', 'message': 'This is a test.'}
        response = self.client.post('/api/send_push_message/', request)
        self.assertEqual(response.status_code, 404)
