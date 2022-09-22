from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserSignIn

def signupRoute(request):
    type = request.GET.get('type', 'null')
    if type == 'client':
        form = UserCreationForm()
        return render(request, 'common/signup_client.html', {'form': form})
    elif type=='partner':
        form=UserCreationForm()
        return render(request,'common/signup_partner.html',{'form':form})
    return render(request,'common/signup.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST.signinForm)
        if form.is_valid():
            print("valid")
            form.save()
            useremail = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=useremail,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/boltnnut/')
        else:
            print("invalid>>>>>>>")
            print(form.errors)
            return redirect('common/signup')
    else:
        type = request.GET.get('type', 'null')
        if type == 'client':
            form = UserCreationForm()
            return render(request, 'common/signup_client.html', {'form': form})
        elif type=='partner':
            form=UserCreationForm()
            return render(request,'common/signup_partner.html',{'form':form})
        else:
            print("null value")
    return render(request,'common/signup.html')
            

def signin(request):
    if request.method=="POST":
        form=UserSignIn(request.POST)
        if form.is_valid():
            print("valid")
            usermail=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(email=usermail,password=password)
            if user is not None:
                login(request,user)
                return redirect('/boltnnut/')
            else:
                return redirect('common:signin')
        else:
            print("invalid")
            print(form)
    form=UserSignIn()
    return render(request,'common/login.html',{'form':form})
    
    
       
