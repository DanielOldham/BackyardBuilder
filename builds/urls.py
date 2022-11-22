from . import views
from django.urls import path

app_name = 'builds'
urlpatterns = [
    path('', views.build_list, name='build_list'),
]