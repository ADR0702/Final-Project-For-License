from django.urls import path
from .views import *

urlpatterns = [
    path("product_list", product_list_view),
    path("product_detail", product_detail_view)
]
