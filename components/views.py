from django.shortcuts import render
from .models import *


# Create your views here.
def search(request):
    context = {}

    components = Component.objects.all()
    context['components'] = components

    return render(request, 'components/search.html', context)
