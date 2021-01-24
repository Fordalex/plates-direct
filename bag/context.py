from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})  
    fitting_kit = False

    for item, dic in bag.items():
        product = item

        item_name = bag[item]['item']

        if item_name == 'both': 
            product_cost = 19.99
        elif item_name == 'front' or item_name == 'back':
            product_cost = 10.99
        elif item_name == 'fitting_kit':
            product_cost = 4.99
        if item_name == 'both' or item_name == 'front' or item_name == 'back':    
            bag_items.append(
                {
                    'reg_number': bag[product]['reg_number'],
                    'item': bag[product]['item'],
                    'cost': product_cost,
                    'quantity': 1,
                    'id': product
                }
            )
        else:
            bag_items.append(
                {
                    'reg_number': 0,
                    'item': 0,
                    'cost': product_cost,
                    'quantity': bag[product]['quantity'],
                    'id': product
                }
            )
            fitting_kit = True
        total += product_cost

    if total < settings.FREE_DELIVERY_THERESHOLD:
        delivery = settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THERESHOLD - total
        grand_total = round(delivery, 2) + round(total, 2)
    else:
        delivery = 0
        free_delivery_delta = 0
        grand_total = round(total, 2)


    context = {
        'bag_items': bag_items,
        'total': round(total, 2),
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': round(free_delivery_delta, 2),
        'free_delivery_threshold': settings.FREE_DELIVERY_THERESHOLD,
        'grand_total': round(grand_total, 2),
        'fitting_kit': fitting_kit, 
    }

    return context