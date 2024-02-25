from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, Order
from django.contrib.messages import get_messages

class ProfileViewTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        UserProfile.objects.create(user=self.user)

        # Create an order for testing order history
        self.order = Order.objects.create(order_number='12345', full_name='Test User', user_profile=UserProfile.objects.get(user=self.user))

    def test_profile_view_requires_login(self):
        # Log out the user
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, f'/accounts/login/?next=/profile/')

    def test_profile_view_with_get_request(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIsInstance(response.context['form'], UserProfileForm)
        self.assertTrue(response.context['on_profile_page'])

    def test_profile_update_with_post_request(self):
        response = self.client.post(reverse('profile'), {
            'default_full_name': 'Updated Name',
        })
        self.assertRedirects(response, reverse('profile'))
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Your profile was updated successfully', str(messages[0]))
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_full_name, 'Updated Name')

class OrderHistoryViewTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        UserProfile.objects.create(user=self.user)

        # Create an order for testing order history
        self.order = Order.objects.create(order_number='12345', full_name='Test User', user_profile=UserProfile.objects.get(user=self.user))

    def test_order_history_view(self):
        response = self.client.get(reverse('order_history', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertTrue('from_profile' in response.context)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(f'This is a past confirmation for order number {self.order.order_number}.' in str(message) for message in messages))