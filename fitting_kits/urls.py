from django.urls import path
from . import views

urlpatterns = [
    path("", views.fitting_kits, name="fitting_kits")
] 