from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from orders.forms import OrderForm
from .models import House

def houses_list(request):
    houses = House.objects.all()

    context = {
        "houses": houses
    }
    return render(request, 'houses/houses_list.html', context=context)


def house_detail(request: HttpRequest, house_id):
    house = get_object_or_404(House, pk=house_id)
    form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        "house": house,
        "form": form
    }
    return render(request, 'houses/house_detail.html', context=context)
