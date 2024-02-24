from django.test import TestCase
from products.models import Product
from django.urls import reverse

class CartViewsTest(TestCase):

    def setUp(self):
        # Creates a mock product
        self.product = Product.objects.create(
            name='Test Product', 
            price=9.99, 
            stock=10
        )

    def test_view_cart(self):
        # Tests the viewing of the cart page
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        # Tests adding an item to the cart
        response = self.client.post(reverse('add_to_cart', args=[self.product.pk]), {
            'quantity': '3', 
            'redirect_url': reverse('view_cart')
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'][str(self.product.pk)], 3)

    def test_update_cart(self):
        # Tests updating the cart
        self.client.post(reverse('add_to_cart', args=[self.product.pk]), {'quantity': '1', 'redirect_url': reverse('view_cart')})
        new_quantity = 2
        response = self.client.post(reverse('update_cart', args=[self.product.pk]), {'quantity': str(new_quantity)})
        
        # Checks if the cart was updated correctly
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'][str(self.product.pk)], new_quantity)

    def test_remove_from_cart(self):
        # Tests removing an item from the cart
        self.client.post(reverse('add_to_cart', args=[self.product.pk]), {'quantity': '1', 'redirect_url': reverse('view_cart')})
        response = self.client.post(reverse('remove_from_cart', args=[self.product.pk]))
        
        # Checks if the item was removed from the cart
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(str(self.product.pk), self.client.session['cart'])
