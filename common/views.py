from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserChangeForm


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            useremail = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=useremail,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        type = request.GET.get('type', 'null')
        if type == 'client':
            form = UserCreationForm()
            return render(request, 'common/signup_client.html', {'form': form})
        elif type=='partner':
            form=UserCreationForm()
            return render(request,'common/signup_partner.html',{'form':form})
    return render(request,'common/signup.html')
            
    
    
       
