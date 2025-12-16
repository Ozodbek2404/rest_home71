from django.urls import path
from .views import (
    category_list_create,
    supplier_list_create,
    product_list_create
)


urlpatterns = [
    path('categories/', category_list_create),
    path('suppliers/', supplier_list_create),
    path('products/', product_list_create),
]
