from django.test import TestCase
from .models import Category, Product
from django.urls import reverse


class ProductViewsTest(TestCase):

    def setUp(self):
        category = Category.objects.create(name='test_category', friendly_name='Test Category')
        Product.objects.create(
            category=category,
            slug='test-product',
            name='Test Product',
            price=9.99,
            stock=10,
            description='Test Description',
            features='Test Features',
            image_url='http://example.com/image.jpg',
            image='test_image.jpg'
        )

    def test_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    def test_product_detail_view(self):
        product = Product.objects.get(slug='test-product')
        response = self.client.get(reverse('product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.context['product'], product)
