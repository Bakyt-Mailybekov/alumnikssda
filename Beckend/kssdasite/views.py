from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
	return render(request, 'kssdasite/index.html')


def projects(request):
	projects = Project.objects.all()
	return render(request, 'kssdasite/projects.html', {'projects': projects})


'''
def about(request):
    alumni = Alumni.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        alumni = Alumni.objects.filter(first_name_alumni=search_query)
    else:
        alumni = Alumni.objects.all()

    return render(request, 'kssdasite/about.html', {'alumnis': alumni})
'''