from django.urls import path
from .views import *

urlpatterns = [
    path("payment", process_payment_view ),
]
