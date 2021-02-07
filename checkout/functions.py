def reg_plate_format(bag):
    formated_bag = []

    for item, dic in bag.items():
        product = item
        item_name = bag[item]['item']
        if item_name == 'both': 
            product_cost = 19.99
        elif item_name == 'front' or item_name == 'back':
            product_cost = 10.99
        if item_name == 'both' or item_name == 'front' or item_name == 'back':    
            formated_bag.append(
                {
                    'reg_number': bag[product]['reg_number'],
                    'quantity': bag[product]['item'],
                    'cost': product_cost,
                }
            )

    return str(formated_bag)
