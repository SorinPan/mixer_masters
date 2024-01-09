from django.test import TestCase
from .models import Category, Product
from decimal import Decimal

class TestCategoryModel(TestCase):

    def setUp(self):
        Category.objects.create(name='test_category', friendly_name='Test Category')

    def test_category_string(self):
        category = Category.objects.get(name='test_category')
        self.assertEqual(str(category), 'test_category')

    def test_get_friendly_name(self):
        category = Category.objects.get(name='test_category')
        self.assertEqual(category.get_friendly_name(), 'Test Category')


class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Test Category', friendly_name='Test Friendly Name')
        Product.objects.create(
            category=Category.objects.get(name='Test Category'),
            slug='test-product',
            sku='TEST123',
            name='Test Product',
            price=9.99,
            rating=5,
            description='Test Description',
            stock=10,
            features='Test Features',
            image_url='http://example.com/image.jpg',
            image='test_image.webp'
        )

    def test_product_creation(self):
        product = Product.objects.get(slug='test-product')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, Decimal('9.99'))

    def test_product_str(self):
        product = Product.objects.get(slug='test-product')
        self.assertEqual(str(product), 'Test Product')

