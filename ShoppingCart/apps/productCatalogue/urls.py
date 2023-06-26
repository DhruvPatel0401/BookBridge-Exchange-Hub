from django.urls import path

from . import views

app_name = "productCatalogue"

urlpatterns = [
    path("", views.ProductAll.as_view(), name="store_home"),
    path("<slug:slug>", views.ProductDetail.as_view(), name="product_detail"),
    path(
        "shop/<slug:category_slug>/", views.CategoryList.as_view(), name="category_list"
    ),
]
