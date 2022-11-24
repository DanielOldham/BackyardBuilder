from . import views
from django.urls import path

app_name = 'builds'
urlpatterns = [
    path('', views.build_list, name='build_list'),
    path('new', views.new_build, name='new_build'),
    path('<int:build_id>', views.view_build, name='view_build'),
    path('<int:build_id>/delete', views.delete_build, name='delete_build'),
]
