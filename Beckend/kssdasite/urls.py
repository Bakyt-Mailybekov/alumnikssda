from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('projects/', views.projects, name='projects_url'),
    path('languages/', views.languages, name='languages_url'),
    path('alumni/', views.alumni, name='alumni_url'),
    path('alumnus/<int:id>/', views.alumnus, name='alumnus_url'),
    path('about/', views.about, name='about_url'),
    #path('index/feedback/', views.feedback, name='feedback'),
]