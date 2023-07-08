from django.urls import path

from . import views

app_name = "basket"

urlpatterns = [
    path("", views.BasketSummary.as_view(), name="basket_summary"),
    path('update-delivery-option/', views.UpdateDeliveryOption.as_view(), name='update_delivery_option'),
    path("add/", views.BaseketAdd.as_view(), name="basket_add"),
    path("delete/", views.BasketDelete.as_view(), name="basket_delete"),
    path("update/", views.BasketUpdate.as_view(), name="basket_update"),
]
