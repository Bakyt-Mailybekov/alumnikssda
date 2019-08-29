from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.index, name='Index'),

    path('projects/', views.projects, name='Projects'),
    path('projects/languages/', views.languages, name='Languages'),
    path('projects/ /', views.index, name='Index'),

    path('languages/', views.languages, name='Languages'),
    path('languages/alumni/', views.alumni, name='Alumni'),
    path('languages/alumni/alumnus/', views.alumnus, name='Alumnus'),
    path('alumnus/', views.alumnus, name='alumnus'),

    path('about/', views.about, name='About'),
]