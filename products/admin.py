from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    list_filter = ['name',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'stock', 'price', 'category',
                    'rating', 'image')
    ordering = ('sku',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
