from django.urls import path
from . import views
from .views import AlumniDetailView

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index_url'),
    path('projects/', views.projects, name='projects_url'),
    path('languages/', views.languages, name='languages_url'),
    path('alumni/', views.alumni, name='alumni_url'),
    path('alumnus/<int:id>/', views.alumnus, name='alumnus_url'),
    path('about/', views.about, name='about_url'),
    #path('index/feedback/', views.feedback, name='feedback'),
=======
    path('', views.index, name='Index'),
    path('feedback/', views.feedback, name='feedback'),
    path('projects/', views.projects, name='Projects'),
    path('projects/languages/', views.languages, name='Languages'),
    path('projects/', views.index, name='Index'),
    path('languages/', views.languages, name='Languages'),
    path('languages/alumni/', views.alumni, name='Alumni'),
    path('languages/alumni/alumnus/', views.alumnus, name='Alumnus'),
    path('alumnus/', views.alumnus, name='alumnus'),
    path('about/', views.about, name='About'),
    path('alumni/<int:pk>/', AlumniDetailView.as_view(), name='alumni')
>>>>>>> b1cd0b3b89e58abb91f870436cb0ceec48a9eeca
]