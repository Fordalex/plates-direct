from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="view_checkout"),
    path("payment/", views.payment_review, name="payment_review"),
    path("add_personal_information/", views.add_personal_information, name="add_personal_information"),
    path("order_complete/", views.order_complete, name="order_complete"),
    path("complete_page/", views.complete_page, name="complete_page"),
] 