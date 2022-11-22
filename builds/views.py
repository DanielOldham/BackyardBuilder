from django.shortcuts import render


# Create your views here.
def build_list(request):
    return render(request, 'builds/build_list.html', {})
