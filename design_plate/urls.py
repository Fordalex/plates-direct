from django.urls import path
from . import views

urlpatterns = [
    path("", views.design_plate, name="design_plates")
] 