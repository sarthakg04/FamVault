# urls.py
from django.urls import path
from . import views
from .views import directory_structure

urlpatterns = [
    path('', views.file_manager, name='file_manager'),
    path('directory/', directory_structure, name='directory_structure'),
]
