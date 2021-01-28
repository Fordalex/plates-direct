from django.shortcuts import render, redirect
from django.conf import settings
import json
import stripe
import os
from os import path
if path.exists('env.py'):
    import env

# Create your views here.
def checkout(request):
    return render(request, 'checkout/checkout.html')

def add_personal_information(request):
    request.session['first_name'] = request.POST.get('first_name')
    request.session['last_name'] = request.POST.get('last_name')
    request.session['email'] = request.POST.get('email')

    request.session['first_line_address'] = request.POST.get('first_line_address')
    request.session['town'] = request.POST.get('town')
    request.session['city'] = request.POST.get('city')
    request.session['post_code'] = request.POST.get('post_code')

    return redirect('payment_review')

def payment_review(request):
    # Stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag_info = request.session.get('bag_info', {})
    if not bag_info:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('design_plates'))

    print('working bag next')
    print(bag_info)

    total = bag_info['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = 'form'
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('api_key'),
        'client_secret': 'test client sceret',
    }

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment')
    
    # Customers information

    first_name = request.session['first_name']
    last_name = request.session['last_name']
    email = request.session['email']
    first_line_address = request.session['first_line_address']
    town = request.session['town']
    city = request.session['city']
    post_code = request.session['post_code']



    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'first_line_address': first_line_address,
        'town': town,
        'city': city,
        'post_code': post_code,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/payment_review.html', context)

def create_payment(request):
    return null