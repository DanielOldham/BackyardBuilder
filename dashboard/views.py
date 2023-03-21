from django.shortcuts import render


def dashboard(request):
    """
    Django view.
    Display dashboard page.

    :param request: Django request
    :return: rendered dashboard template
    """
    return render(request, 'dashboard/dashboard.html', {})
