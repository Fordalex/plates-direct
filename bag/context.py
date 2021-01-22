from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item, value in bag.items():
        product = item
        if product == 'both' or 'front' or 'back':
            for reg in value:
                if product == 'both': 
                    product_cost = 19.99
                elif product == 'front' or 'back':
                    product_cost = 10.99
                elif product == 'fitting_kit':
                    product_cost = 4.99

                total += product_cost

                bag_items.append({
                    'item': product,
                    'quantity': 1,
                    'reg_number': value[0],
                    'cost': product_cost
                })
        

    if total < settings.FREE_DELIVERY_THERESHOLD:
        delivery = total + settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THERESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THERESHOLD,
        'grand_total': grand_total,
    }

    return context