from django.test import TestCase

from django.urls import reverse

class CartViewsTest(TestCase):

    def test_view_cart(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
    
    def test_add_to_cart(self):
        item_id = 'some-item-id'  # Replace with a valid item ID
        quantity = 3
        response = self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': quantity, 'redirect_url': reverse('view_cart')
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'][item_id], quantity)
