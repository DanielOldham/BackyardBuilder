from . import views
from django.urls import path

app_name = 'builds'
urlpatterns = [
    path('', views.build_list, name='build_list'),
    path('new', views.new_build, name='new_build'),
    path('new/<int:component_id>', views.new_build_component, name='new_build_component'),
    path('<int:build_id>', views.view_build, name='view_build'),
    path('<int:build_id>/delete', views.delete_build, name='delete_build'),
    path('<int:build_id>/<str:component_type>/remove', views.remove_component, name='remove_component'),
    path('<int:build_id>/<int:component_id>/add', views.add_component, name='add_component'),
]
