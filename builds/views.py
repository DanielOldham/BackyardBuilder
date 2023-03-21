from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Build
from .forms import BuildNameForm
from components.models import Component


@login_required
def build_list(request):
    """
    Django view.
    Display a list of the current user's builds

    :param request: Django request
    :return: rendered build_list template
    """
    context = {}

    user = request.user
    builds = Build.objects.filter(user=user)
    context['builds'] = builds

    return render(request, 'builds/build_list.html', context)


@login_required
def new_build(request):
    """
    Create new build belonging to current user.

    :param request: Django request
    :return: redirect to builds:view_build
    """
    user = request.user
    build = Build.objects.create(user=user)

    return redirect('builds:view_build', build.id)


@login_required
def view_build(request, build_id):
    """
    Django view.
    Display a detailed view of one specific build belonging to a user.

    :param request: Django request
    :param build_id: id of the build to display
    :return: redirect to builds:build_list
    """
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
    """
    Django view.
    Delete the build associated with the given build_id.

    :param request: Django request
    :param build_id: id of the build to delete
    :return: redirect to builds:build_list
    """
    build = Build.objects.get(id=build_id)

    # just double check to make sure the build belongs to the user
    if request.user == build.user:
        build.delete()

    return redirect('builds:build_list')


@login_required
def remove_component(request, build_id, component_type):
    """
    Django view.
    Remove specific component from the given build.

    :param request: Django request.
    :param build_id: id of the build to remove component from
    :param component_type: type of component to remove from build
    :return: redirect to builds:view_build
    """
    build = Build.objects.get(id=build_id)

    # if the build doesn't belong to that user, redirect back to dashboard
    if request.user != build.user:
        return redirect('builds:build_list')

    build.__setattr__(component_type, None)
    build.save()
    return redirect('builds:view_build', build.id)


@login_required
def add_component(request, build_id, component_id):
    """
    Django view.
    Add specific component to a user's build.

    :param request: Django request
    :param build_id: id of the build to add component to
    :param component_id: id of the component to add
    :return: redirect to builds:build_list
    """
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
    """
    Django view.
    Create a new build and add the associated component.

    :param request: Django request
    :param component_id: id of the component to add to the new build
    :return: redirect to builds:view_build
    """
    build = Build.objects.create(user=request.user)
    component = Component.objects.get(id=component_id)

    build.__setattr__(component.get_type().lower(), component.get_child())
    build.save()

    return redirect('builds:view_build', build.id)
