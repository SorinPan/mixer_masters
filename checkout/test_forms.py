from django.test import TestCase
from .forms import OrderForm

class TestOrderForm(TestCase):

    def test_order_form_placeholder_and_attrs(self):
        """Test form placeholders and custom attributes are set correctly."""
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertEqual(form.fields['full_name'].widget.attrs['autofocus'], True)

    def test_order_form_validation(self):
        """Test the OrderForm with valid and invalid data."""
        valid_data = {
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'email': 'john@example.com',
            'street_address1': '123 Main St',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'county': 'Anycounty',
            'country': 'US',
        }

        form = OrderForm(data=valid_data)
        self.assertTrue(form.is_valid())

        invalid_data = valid_data.copy()
        invalid_data['email'] = 'not-an-email'

        form = OrderForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
