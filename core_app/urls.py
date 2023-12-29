from django.urls import path
from .views import laptops_list

urlpatterns = [
    path('', laptops_list, name='laptops_list'),
]
