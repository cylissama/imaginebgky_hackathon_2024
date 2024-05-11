from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('/complaints/', complaint_view, name="complaints"),
    path('/vendors/', add_vendor_view, name='vendor')
]
