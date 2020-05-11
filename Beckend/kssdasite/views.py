from django.views.generic import DetailView
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
	return render(request, 'kssdasite/index.html')

def feedback(request):
    return render(request, 'kssdasite/feedback.php')

def projects(request):
	projects = Project.objects.all()
	return render(request, 'kssdasite/projects.html', {'projects': projects})

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

    '''search_query = request.GET.get('search', '')
    if search_query:
        alumni = Alumni.objects.filter(first_name_alumni=search_query)
    else:
        alumni = Alumni.objects.all()
'''

