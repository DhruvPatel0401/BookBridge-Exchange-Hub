from django.urls import path
from . import views

app_name = "baket"

urlpatterns = [
    path("", views.BasketSummary.as_view(), name = "basket_summary"),
]
