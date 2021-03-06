from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ( 'date','first_name',
              'email', 'phone_number', 'county',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total','order_number','reg_plate')

    fields = ('order_made', 'order_dispatch', 'date','first_name','reg_plate',
              'email', 'phone_number', 'county',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total','order_number',)

    list_display = ('date','order_made', 'order_dispatch', 'first_name',
                    'grand_total',)

    ordering = ('-date',)

    change_list_template = 'admin/send_order_confirmation.html'

    # change_form_template = 'admin/send_order_confirmation.html'

admin.site.site_header = 'Plates Direct'
admin.site.register(Order, OrderAdmin)
admin.site.unregister(Group)

