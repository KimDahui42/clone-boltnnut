from unicodedata import category
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Project,Partners,ProjectFile
from common.models import User
from .forms import UploadProjectForm
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
        form=UploadProjectForm(request.POST)
        
        if form.is_valid():
            print("valid")
            user=uploadSignup(request)
            form.save()
            key=Project.objects.last()
            uploadFiles(request,key)
            print(request.FILES)
        else:
            print(form)
    else:
        form=UploadProjectForm()
        return render(request, 'mainsite/uploadProject.html',{'form':form})
    return redirect('/boltnnut/uploadProject')


def uploadFiles(request,key):
    files=request.FILES.getlist('attached')
    print(key)
    print(files)
    for f in files:
        tmp=ProjectFile.objects.create(file=f,project=key)
        tmp.save()
    return redirect('/boltnnut/')

def uploadSignup(request):
    signup_form=request.POST
    user=User()
    user.email=signup_form['email']
    user.company=signup_form['company']
    user.userType='client'
    password=signup_form['password1']
    password2=signup_form['password2']
    if password==password2:
        user.password=password
    else:
        return
    user.name=signup_form['name']
    user.phone=signup_form['phone']
    user.jobPosition=signup_form['jobPosition']
    user.save()
    return user

def search(request):
    context = {

    }
    return render(request, 'mainsite/search.html', context)


def services(request):
    context = {

    }
    return render(request, 'mainsite/services.html', context)