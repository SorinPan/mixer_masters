from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    """
    Add and edit line items in the admin order
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('date', 'order_number',
                       'order_total', 'shipping_cost',
                       'grand_total', 'original_cart',
                       'stripe_pid',)

    fields = ('user_profile', 'full_name', 'phone_number',
              'email', 'street_address1', 'street_address2',
              'town_or_city', 'postcode', 'county', 'country',
              'date', 'order_number', 'order_total', 
              'shipping_cost', 'grand_total',
              'original_cart', 'stripe_pid',)

    list_display = ('full_name', 'date', 'order_number',
                    'order_total', 'shipping_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
