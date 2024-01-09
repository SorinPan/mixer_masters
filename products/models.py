from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=100, unique=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.PositiveSmallIntegerField(null=True)
    description = models.TextField()
    stock = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    features = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
