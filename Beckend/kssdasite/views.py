from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import *
from .models import Project


# Create your views here.


def index(request):
    return render(request, 'kssdasite/index.html')


def feedback(request):
    return render(request, 'kssdasite/feedback.php')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'kssdasite/projects.html', {'projects': projects})


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'kssdasite/project_detail_view.html'
    context_object_name = 'project'


def languages(request):
    return render(request, 'kssdasite/languages.html')


def alumni(request):
    alumnis = Alumni.objects.all()
    return render(request, 'kssdasite/alumni.html', {'alumnis': alumnis})


class AlumniDetailView(DetailView):
    model = Alumni
    template_name = 'kssdasite/alumni_detail_view.html'
    context_object_name = 'alumni'


def alumnus(request):
    alumnis = Alumni.objects.all()
    return render(request, 'kssdasite/alumnus.html', {'alumnis': alumnis})


def about(request):
    alumnis = Alumni.objects.all()
    return render(request, 'kssdasite/about.html', {'alumnis': alumnis})


class AdsView(ListView):
    model = Ads
    template_name = 'kssdasite/ads.html'
    context_object_name = 'ads'

class AdDetailView(DetailView):
    model = Ads
    template_name = 'kssdasite/ads_detail_view.html'
    context_object_name = 'ad'