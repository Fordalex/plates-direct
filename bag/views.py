from django.shortcuts import render, redirect
import random
from django.contrib import messages

# Create your views here.
def view_bag(request):
    """ Display the shopping basket page. """
    request.session['redirect_url'] = request.path
    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add the item to the shopping basket in the session. """

    redirect_url = request.session['redirect_url']
    bag = request.session.get('bag', {})
    id_count = request.session.get('id_count', 0)
    reg_number = request.POST.get('reg_number')
    item = request.POST.get('item')
    fitting_kit = request.POST.get('fitting-kit')

    if fitting_kit == 'on':
        if 'fitting_kit' in list(bag.keys()):
            bag['fitting_kit']['quantity'] += 1
        else:
            bag['fitting_kit'] = {'quantity': 1, 'item': 'fitting_kit'}
        messages.success(request, f'Added a fitting kit to your bag.')

    try:
        if len(reg_number) > 2:
            bag[id_count] = {
                    'reg_number': reg_number,
                    'item': item,
                }
    except:
        print('no reg')

    messages.success(request, f'Added {item} UK Registration to your bag.')

    request.session['bag'] = bag
    id_count += 1
    request.session['id_count'] = id_count

    return redirect(redirect_url)


def remove_from_bag(request, reg):
    """ Remove the item form the shopping bag and return the user to the shopping bag page. """
    bag = request.session.get('bag', {})
    bag.pop(reg)
    request.session['bag'] = bag
    return redirect('view_bag')


def empty_basket(request):
    """ Empty the users shopping basket. """
    request.session['bag'] = {}
    request.session['bag_info'] = {}
    return redirect('view_bag')