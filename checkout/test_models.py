from django.test import TestCase
from django.conf import settings
from .models import Order, OrderLineItem, Product, UserProfile
from django_countries.fields import CountryField

class TestModels(TestCase):

    def create_order(self):
        """
        Helper method to create an order instance.
        """
        order = Order.objects.create(
            full_name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            street_address1='123 Main St',
            town_or_city='Anytown',
            country='US',
            county='Anycounty',
        )
        return order

    def test_order_number_generated_on_save(self):
        """
        Test that an order number is generated on saving an order.
        """
        order = self.create_order()
        self.assertIsNotNone(order.order_number)
        self.assertTrue(len(order.order_number) > 0)

    def test_order_update_total(self):
        """
        Test the update_total method of the Order model.
        """
        order = self.create_order()
        product = Product.objects.create(
            name='Test Product',
            price=10.00
        )
        OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=2
        )
        order.update_total()
        self.assertEqual(order.order_total, 20.00)

    def test_lineitem_total_calculation(self):
        """
        Test that lineitem total is calculated correctly on saving.
        """
        order = self.create_order()
        product = Product.objects.create(
            name='Test Product',
            price=10.00
        )
        line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=2
        )
        self.assertEqual(line_item.lineitem_total, 20.00)

    def test_order_str(self):
        """
        Test the string representation of the Order model.
        """
        order = self.create_order()
        self.assertEqual(str(order), order.order_number)

    def test_orderlineitem_str(self):
        """
        Test the string representation of the OrderLineItem model.
        """
        order = self.create_order()
        product = Product.objects.create(
            name='Test Product',
            price=10.00
        )
        line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=1
        )
        expected_str = f'SKU {product.sku} on order {order.order_number}'
        self.assertEqual(str(line_item), expected_str)
