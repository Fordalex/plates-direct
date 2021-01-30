from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date')

    fields = ('order_number', 'date','full_name',
              'email', 'phone_number', 'county',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
    