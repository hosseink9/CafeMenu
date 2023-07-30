from django.urls import path
from .views import *


app_name = "orders"


urlpatterns = [
    path("order_list/", order_list, name="order_list"),
    path("order_details/<int:id>/", order_details, name="order_details"),
    path("cart/",cart, name="cart"),
    path("", index, name="index")
]