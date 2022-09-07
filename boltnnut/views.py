from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project,Partners
from django.template import RequestContext

def index(request):
    category=['전자/반도체 부품','생활/위생','디지털/가전','반려','인테리어','주방','볼트/너트류','동력전달부품','냉난방/공조','밴딩/포장']
    context={
        'items':category
    }
    data={}
    for i in category:
        try:
            data[i]=Partners.objects.get(category=i)[3]
        except Partners.DoesNotExist:
            data[i]='null'

    context['data']=data
    return render(request, 'mainsite/index.html', context)


def projects(request):
    context = {

    }
    return render(request, 'mainsite/projects.html', context)


def upload(request):
    if request.method=="POST":
        form=request.POST
        projectData=Project()
        projectData.title=form['title']
        projectData.budget=form['budget']
        #projectData.budget_show=form['budget_show']
        projectData.expired_date=form['expired_date']
        #projectData.expired_negotiate=form['expired_negotiate']
        projectData.goal=form['goal']
        #projectData.goal_negotiate['goal_negotiate']
        projectData.descript=form['descript']
        projectData.attached=form['attached']
        projectData.save()
        return render(request,'mainsite/uploadProject.html',{'status':'done'})

    return render(request, 'mainsite/uploadProject.html',{'status':'ongoing'})


def search(request):
    context = {

    }
    return render(request, 'mainsite/search.html', context)


def services(request):
    context = {

    }
    return render(request, 'mainsite/services.html', context)