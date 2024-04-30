from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Manager
from .views import createPass, edit_data

class TestManPassword(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='StrongPassword123!')
        self.factory = RequestFactory()
        self.manager1 = Manager.objects.create(user=self.user, category='Category 1', password='password1', description='Description 1')
        self.manager2 = Manager.objects.create(user=self.user, category='Category 2', password='password1', description='Description 1')

    def test_showpass_view(self):
        self.client.login(username='testuser', password='StrongPassword123!')
        
        response = self.client.get(reverse('manPassword:showpass'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'passInfo.html')
        
        self.assertTrue('managers' in response.context)
        
        managers = response.context['managers']
        self.assertEqual(len(managers), 2)
        self.assertEqual(managers[0].category, 'Category 1')
        self.assertEqual(managers[1].category, 'Category 2')

    def test_filter_view(self):
        response = self.client.get(reverse('manPassword:filter'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'passInfo.html')
        self.assertTrue('managers' in response.context)
        
        managers = response.context['managers']
        self.assertEqual(len(managers), 2)

    def test_createpass_view_get(self):
        response = self.client.get(reverse('manPassword:createPass'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'createPass.html')

    def test_createpass_view_post(self):
        request = self.factory.post(reverse('manPassword:createPass'), {
            'category': 'Category 4',
            'password': 'password1',
            'description': 'Description 1',
        })
        request.user = self.user
        response = createPass(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('user:home'))

        self.assertTrue(Manager.objects.filter(user=self.user, category='Category 4').exists())
    
    def test_delete_view(self):
        self.client.login(username='testuser', password='StrongPassword123!')
        
        response = self.client.post(reverse('manPassword:delete', kwargs={'id': self.manager1.pk}))
        
        self.assertEqual(response.status_code, 302)
        
        manager_exists = Manager.objects.filter(pk=self.manager1.pk).exists()
        self.assertFalse(manager_exists)
    
    def test_edit_data_view_get(self):


        response = self.client.get(reverse('manPassword:edit_data', kwargs={'data_id': self.manager1.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_data.html/')
        self.assertTrue('form' in response.context)
        self.assertEqual(response.context['form'].instance, self.manager1)

