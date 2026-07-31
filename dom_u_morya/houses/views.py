from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from orders.forms import OrderForm
from .forms import HouseFilterForm
from .models import House

def houses_list(request):
    houses = House.objects.filter(active=True)
    house_filter_form = HouseFilterForm(request.GET)

    if house_filter_form.is_valid():
        cd = house_filter_form.cleaned_data
        min_price, max_price, query = cd['min_price'], cd['max_price'], cd['query']
    
        if min_price:
            houses = houses.filter(price__gte=min_price)
        if max_price:
            houses = houses.filter(max_price__lte=max_price)
        if query:
            houses = houses.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        "houses": houses,
        'house_filter_form': house_filter_form
    }
    return render(request, 'houses/houses_list.html', context=context)


def house_detail(request: HttpRequest, house_id):
    house = get_object_or_404(House, pk=house_id, active=True)
    form = OrderForm(request.POST or None, initial={'house': house})
    sent = request.GET.get('sent', 0)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        url = reverse('house_detail', args=[house_id])
        return redirect(f"{url}?sent=1")

    context = {
        "house": house,
        "form": form,
        "sent": sent
    }
    return render(request, 'houses/house_detail.html', context=context)
