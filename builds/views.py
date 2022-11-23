from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Build


# Create your views here.
@login_required
def build_list(request):
    context = {}

    user = request.user
    builds = Build.objects.filter(user=user)
    context['builds'] = builds

    #context['costs'] = [build.total_price() for build in builds]

    return render(request, 'builds/build_list.html', context)


@login_required
def new_build(request):
    context = {}

    user = request.user
    build = Build.objects.create(user=user)

    context['build'] = build

    return render(request, 'builds/build_view.html', context)
