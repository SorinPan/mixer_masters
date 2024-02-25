from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Order, Product, UserProfile
from django.contrib.auth.models import User

class CheckoutViewTests(TestCase):

    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=10)

    def test_checkout_view_with_empty_cart(self):
        # Simulate a logged-in user
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('products'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your cart is currently empty")

    def test_cache_checkout_data(self):
        self.client.login(username='testuser', password='testpass')
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'test_secret_123_secret',
            'save_info': 'true',
        })
        self.assertEqual(response.status_code, 200)

    def test_checkout_success(self):
        order = Order.objects.create(
            full_name='John Doe',
            email='john@example.com',
            phone_number='123456789',
            street_address1='123 Street',
            town_or_city='Town',
            country='US'
        )
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Order successfully processed!', str(messages[0]))