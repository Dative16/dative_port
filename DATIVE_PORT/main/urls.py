from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('projects/', views.project_list, name='project_list'),
    path('research/', views.research_list, name='research_list'),
]
