from django.urls import path

from . import views

app_name='boltnnut'

urlpatterns = [
    path('', views.index),
    path('projects',views.projects,name='projects'),
    path('uploadProject',views.upload,name='uploadProject'),
    path('search',views.search,name='search'),
    path('services',views.services,name='services'),
]