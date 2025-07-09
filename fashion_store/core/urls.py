from django.urls import path
from .views import *

urlpatterns = [

    path("all", home_view),
    path("details", home_details_view),

]
