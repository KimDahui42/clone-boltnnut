from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from .models import User,CustomUserManager


class UserCreationForm(forms.ModelForm):
    email=forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':_('boltnnut@gmail.com'),
                'required':'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':_('비밀번호를 입력해 주세요.'),
                'required':'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'), 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':_('비밀번호를 한 번 더 입력해 주세요.'),
                'required':'True',
            }
        )
    )
    name=forms.CharField(
        label=_('name'),
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':_('이름을 입력해 주세요.'),
                'required':'True',
            }
        )
    )
    phone=forms.CharField(
        label=_('phone number'),
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':_('- 없이 숫자만 입력해 주세요.(최대 11자리)'),
                'required':'True',
            }
        )
    )
    company=forms.CharField(
        label=_('company name'),
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':_('근무하고 계신 회사명을 입력해 주세요.'),
                'required':'True',
            }
        )
    )
    jobPosition=forms.CharField(
        label=_('job position'),
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':_('직급을 입력해 주세요.'),
                'required':'True',
            }
        )
    )
    class Meta:
        model = User
        fields = ('email','company','name','userType','phone','jobPosition')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm).save(commit=False)
        user.email=CustomUserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model=User
        fields=('email','password','company','name','userType','is_active','is_admin')
    
    def clean_password(self):
        return self.initial["password"]