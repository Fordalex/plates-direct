from django.shortcuts import render, redirect
import random

# Create your views here.
def view_bag(request):
    """ Display the shopping basket page. """
    print(request.session['bag'])
    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add the item to the shopping basket in the session. """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    id_count = request.session.get('id_count', 0)
    reg_number = request.POST.get('reg_number')
    item = request.POST.get('item')

    # if item in list(bag.keys()):
    #     bag[item] += [reg_number]
    # else:
    #     bag[item] = [reg_number]

    if reg_number in bag.keys():
        bag[id_count] = {
                'reg_number': reg_number,
                'plates': item,
            }
    else:
        bag[id_count] = {
            'reg_number': reg_number,
            'plates': item,
        }

    print(request.session['bag'])

    request.session['bag'] = bag
    id_count += 1
    request.session['id_count'] = id_count
    return redirect(redirect_url)


def remove_from_bag(request, reg):
    """ Remove the item form the shopping bag and return the user to the shopping bag page. """
    bag = request.session.get('bag', {})

    bag.pop(reg)

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect('view_bag')


def empty_basket(request):
    """ Empty the users shopping basket. """
    request.session['bag'] = {}
    return redirect('view_bag')