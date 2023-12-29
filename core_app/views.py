from django.shortcuts import render
from .models import Laptops


def laptops_list(request):
    laptops = Laptops.objects.all()
    context = {
        'laptops': laptops,
        'title': 'Ноутбуки',
    }
    return render(request, 'core_app/laptop_list.html', context=context)
