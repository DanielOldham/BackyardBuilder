from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Build
from .forms import BuildNameForm
from components.models import Component


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
    user = request.user
    build = Build.objects.create(user=user)

    return redirect('builds:view_build', build.id)


@login_required
def view_build(request, build_id):
    context = {}

    build = Build.objects.get(id=build_id)

    # user should not be able to view a build that isn't theirs
    if build.user != request.user:
        return redirect('builds:build_list')

    context['build'] = build

    form = BuildNameForm(request.POST or None, instance=build)

    if form.is_valid():
        form.save()
        return redirect('builds:view_build', build.id)

    context['form'] = form
    return render(request, 'builds/build_view.html', context)


@login_required
def delete_build(request, build_id):
    build = Build.objects.get(id=build_id)

    # just double check to make sure the build belongs to the user
    if request.user == build.user:
        build.delete()

    return redirect('builds:build_list')


@login_required
def remove_component(request, build_id, component_type):
    build = Build.objects.get(id=build_id)

    # if the build doesn't belong to that user, redirect back to dashboard
    if request.user != build.user:
        return redirect('builds:build_list')

    build.__setattr__(component_type, None)
    build.save()
    return redirect('builds:view_build', build.id)


@login_required
def add_component(request, build_id, component_id):
    build = Build.objects.get(id=build_id)

    # if the build doesn't belong to that user, redirect back to dashboard
    if request.user != build.user:
        return redirect('builds:build_list')

    component = Component.objects.get(id=component_id)

    build.__setattr__(component.get_type().lower(), component.get_child())
    build.save()

    return redirect('builds:view_build', build_id)


@login_required
def new_build_component(request, component_id):
    build = Build.objects.create(user=request.user)
    component = Component.objects.get(id=component_id)

    build.__setattr__(component.get_type().lower(), component.get_child())
    build.save()

    return redirect('builds:view_build', build.id)
