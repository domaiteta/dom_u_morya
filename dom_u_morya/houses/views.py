from django.shortcuts import render, get_object_or_404
from .models import House

def houses_list(request):
    houses = House.objects.all()

    context = {
        "houses": houses
    }
    return render(request, 'houses/houses_list.html', context=context)


def house_detail(request, house_id):
    house = get_object_or_404(House, pk=house_id)

    context = {
        "house": house
    }
    return render(request, 'houses/house_detail.html', context=context)
