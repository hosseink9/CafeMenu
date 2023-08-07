from django.urls import path
from .views import *


app_name = "panel"


urlpatterns = [
    path("",dashboard_staff, name="dashboard_staff"),
    path("order/edit/<int:order_id>/", edit_order, name="edit_order"),
    path("order/approve/<int:order_id>/", approve_order, name="approve_order"),
    path("order/reject/<int:order_id>/", reject_order, name="reject_order"),
]