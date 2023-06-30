from django.urls import path

from . import views

app_name = "basket"

urlpatterns = [
    path("", views.BasketSummary.as_view(), name="basket_summary"),
    path("add/", views.BaseketAdd.as_view(), name="basket_add"),
]
