from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project,Partners

def index(request):
    category=['전자/반도체 부품','생활/위생','디지털/가전','반려','인테리어','주방','볼트/너트류','동력전달부품','냉난방/공조','밴딩/포장']
    context={
        'items':category
    }
    data={}
    for i in category:
        data[i]=Partners.objects.filter(category=i)[3]
    context['data']=data
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