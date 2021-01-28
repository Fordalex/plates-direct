from django.shortcuts import render, redirect
import json
import stripe
import os
from os import path
if path.exists('env.py'):
    import env

stripe.api_key = os.environ.get('api_key')

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
        'stripe_public_key': os.environ.get('api_key'),
        'client_secret': 'test test test',
    }

    return render(request, 'checkout/payment_review.html', context)

def create_payment(request):
    return null