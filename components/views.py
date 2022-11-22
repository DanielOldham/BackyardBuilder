from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def search(request):
    context = {}
    components = []

    # get all form items
    case_box = request.GET.get('caseCheck')
    cooler_box = request.GET.get('coolerCheck')
    cpu_box = request.GET.get('cpuCheck')
    graphics_box = request.GET.get('graphicsCheck')
    mobo_box = request.GET.get('moboCheck')
    power_box = request.GET.get('powerCheck')
    ram_box = request.GET.get('ramCheck')
    storage_box = request.GET.get('storageCheck')

    keyword_input = request.GET.get('keywordInput')
    lower_price_input = request.GET.get('lowerPriceInput')
    upper_price_input = request.GET.get('upperPriceInput')

    if lower_price_input is not None and lower_price_input != '':
        lower_price_bound = float(lower_price_input)
    else:
        lower_price_bound = None
    if upper_price_input is not None and upper_price_input != '':
        upper_price_bound = float(upper_price_input)
    else:
        upper_price_bound = None

    # filter on check boxes
    if case_box is not None:
        cases = Case.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            cases = cases.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            cases = cases.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            cases = cases.filter(name__icontains=keyword_input)

        components += cases
    if cooler_box is not None:
        coolers = Cooler.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            coolers = coolers.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            coolers = coolers.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            coolers = coolers.filter(name__icontains=keyword_input)

        components += coolers
    if cpu_box is not None:
        cpus = CPU.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            cpus = cpus.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            cpus = cpus.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            cpus = cpus.filter(name__icontains=keyword_input)

        components += cpus
        # query_sets.append(cpus)
    if graphics_box is not None:
        graphics = Graphics.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            graphics = graphics.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            graphics = graphics.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            graphics = graphics.filter(name__icontains=keyword_input)

        components += graphics
    if mobo_box is not None:
        mobos = Motherboard.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            mobos = mobos.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            mobos = mobos.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            mobos = mobos.filter(name__icontains=keyword_input)

        components += mobos
    if power_box is not None:
        psus = PowerSupply.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            psus = psus.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            psus = psus.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            psus = psus.filter(name__icontains=keyword_input)

        components += psus
    if ram_box is not None:
        rams = RAM.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            rams = rams.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            rams = rams.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            rams = rams.filter(name__icontains=keyword_input)

        components += rams
    if storage_box is not None:
        storages = Storage.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            storages = storages.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            storages = storages.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            storages = storages.filter(name__icontains=keyword_input)

        components += storages

    # if none are checked, we assume we should show all
    if (case_box is None and cooler_box is None and cpu_box is None and graphics_box is None and mobo_box is None and
            power_box is None and ram_box is None and storage_box is None):
        components = Component.objects.all()

        # filter on price and keyword
        if lower_price_bound is not None:
            components = components.filter(price__gt=lower_price_bound)
        if upper_price_bound is not None:
            components = components.filter(price__lt=upper_price_bound)

        if keyword_input is not None and keyword_input != '':
            components = components.filter(name__icontains=keyword_input)

    # paginator
    paginator = Paginator(components, 4)
    page = request.GET.get('page')
    component_paginator = paginator.get_page(page)

    context['components'] = component_paginator
    return render(request, 'components/search.html', context)


def detail(request, component_id):
    context = {}

    component = Component.objects.get(id=component_id)
    context['component'] = component

    return render(request, 'components/detail.html', context)
