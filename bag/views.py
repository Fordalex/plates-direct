from django.shortcuts import render, redirect
import random

# Create your views here.
def view_bag(request):
    """ Display the shopping basket page. """
    print(request.session['bag'])
    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add the item to the shopping basket in the session. """

    bag = {}

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    reg_number = request.POST.get('reg_number')
    item = request.POST.get('item')

    # if item in list(bag.keys()):
    #     bag[item] += [reg_number]
    # else:
    #     bag[item] = [reg_number]

    if reg_number in bag.keys():
        bag[reg_number + ' Duplicate' + str(random.randint(999, 99999))] = {
                'reg_number': reg_number,
                'plates': item,
            }
    else:
        bag[reg_number] = {
            'reg_number': reg_number,
            'plates': item,
        }


    request.session['bag'] = bag
    print(request.session['bag'])
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