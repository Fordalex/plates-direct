from django.shortcuts import render

# Create your views here.
def design_plate(request):
    request.session['redirect_url'] = request.path 

    return render(request, 'design_plate/design_plates.html')