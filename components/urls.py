from . import views
from django.urls import path

app_name = 'components'
urlpatterns = [
    path('', views.search, name='search'),
    path('<int:component_id>', views.detail, name='detail'),
]