from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Build
from .forms import BuildNameForm


# Create your views here.
@login_required
def build_list(request):
    context = {}

    user = request.user
    builds = Build.objects.filter(user=user)
    context['builds'] = builds

    return render(request, 'builds/build_list.html', context)


@login_required
def new_build(request):
    context = {}

    user = request.user
    build = Build.objects.create(user=user)
    context['build'] = build

    return render(request, 'builds/build_view.html', context)


@login_required
def view_build(request, build_id):
    context = {}

    build = Build.objects.get(id=build_id)
    context['build'] = build

    form = BuildNameForm(request.POST or None, instance=build)

    if form.is_valid():
        form.save()
        return redirect('builds:view_build', build_id)

    context['form'] = form
    return render(request, 'builds/build_view.html', context)


@login_required
def delete_build(request, build_id):
    build = Build.objects.get(id=build_id)

    # just double check to make sure the build belongs to the user
    if request.user == build.user:
        build.delete()

    return redirect('builds:build_list')
