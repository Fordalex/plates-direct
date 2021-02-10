from django.shortcuts import render

# Create your views here.
def fitting_kits(request):
    return render(request, 'fitting_kits/fitting_kits.html')