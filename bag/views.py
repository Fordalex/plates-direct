from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request):

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    reg_number = request.POST.get('reg_number')
    item = request.POST.get('item')

    if item in list(bag.keys()):
        bag[item] += [reg_number]
    else:
        bag[item] = [reg_number]

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)