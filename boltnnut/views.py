from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    context = {
            
    }
    return render(request, 'mainsite/index.html', context)


def projects(request):
    context = {

    }
    return render(request, 'mainsite/projects.html', context)


def upload(request):
    context = {

    }
    return render(request, 'mainsite/uploadProject.html', context)


def search(request):
    context = {

    }
    return render(request, 'mainsite/search.html', context)


def services(request):
    context = {

    }
    return render(request, 'mainsite/services.html', context)