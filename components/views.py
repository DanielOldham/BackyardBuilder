from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.apps import apps


# Create your views here.
def search(request):
    context = {}
    paginate = True

    # get all form items
    radio_input = request.GET.get('componentRadio')
    if radio_input is not None:
        search_model = apps.get_model('components', radio_input)
        if radio_input != 'Component':
            paginate = False
    else:
        search_model = apps.get_model('components', 'Component')

    components = search_model.objects.all()

    keyword_input = request.GET.get('keywordInput')
    lower_price_input = request.GET.get('lowerPriceInput')
    upper_price_input = request.GET.get('upperPriceInput')

    # filter on price
    if lower_price_input is not None and lower_price_input != '':
        components = components.filter(price__gt=float(lower_price_input))
        paginate = False
    if upper_price_input is not None and upper_price_input != '':
        components = components.filter(price__lt=float(upper_price_input))
        paginate = False

    # filter on keyword
    if keyword_input is not None and keyword_input != '':
        components = components.filter(name__icontains=keyword_input)
        paginate = False

    # paginator
    if paginate:
        paginator = Paginator(components, 4)
        page = request.GET.get('page')
        component_paginator = paginator.get_page(page)

        context['components'] = component_paginator
    else:
        context['components'] = components

    context['paginate'] = paginate
    return render(request, 'components/search.html', context)


def detail(request, component_id):
    context = {}

    component = Component.objects.get(id=component_id)
    context['type'] = component.get_type()
    context['component'] = component.get_child()

    return render(request, 'components/detail.html', context)
