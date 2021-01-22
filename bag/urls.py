from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add/", views.add_to_bag, name="add_to_bag"),
    path("remove/<reg>", views.remove_from_bag, name="remove_from_bag"),
    path("empty_basket/", views.empty_basket, name="empty_basket"),
] 