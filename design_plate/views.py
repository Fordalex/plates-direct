from django.shortcuts import render

# Create your views here.
def design_plate(request):
    return render(request, 'design_plate/design_plates.html')