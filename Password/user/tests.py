from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
class TestUser(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='StrongPassword123!')

    def test_signup_post(self):
        response = self.client.post(reverse('user:signup'), {
            'username': 'testuser1234',
            'password1': 'Strongpassword123',
            'password2': 'Strongpassword123',
            'email': 'testuser123@gmail.com', 
        })

        self.assertTrue(User.objects.filter(username='testuser1234').exists())

    def test_home(self):
        response = self.client.get(reverse('user:home'))
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertEqual(response.url, '/accounts/login/?next=/')
        self.assertEqual(response.status_code, 302)

    def test_signup_get(self):
        response = self.client.get(reverse('user:signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('user:logout'))

        self.assertFalse(response.wsgi_request.user.is_authenticated)

        self.assertRedirects(response, reverse('user:login'))