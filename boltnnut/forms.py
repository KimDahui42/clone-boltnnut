'''
 title,
    budget,
    budget_show,
    expired_date,
    expired_negotiation,
    goal,
    goal_negotiation,
    descript,
    attached,
'''
from datetime import date
from django import forms
from .models import Project

class UploadProjectForm(forms.ModelForm):
    title=forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'name':'title',
                'placeholder':'진행하는 프로젝트 제목을 입력해주세요. ex)반려동물 샤워기'
            }
        ),
        initial='title'
    )
    budget=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'name':'budget',
            }
        ),
        initial=0
    )
    budget_show=forms.BooleanField(
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'name':'budget_show',
                }
        )
    )
    expired_date=forms.DateField(
        widget=forms.DateInput(
            attrs={
                'name':"expired_date",
                'placeholder':"날짜를 선택해주세요."
            }
        ),
        initial=date.today()
    )
    expired_negotiate=forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'name':'expired_negotiate',
        })
    )
    goal=forms.IntegerField(
        widget=forms.DateInput(
            attrs={
                'name':"goal",
                'placeholder':"숫자로 입력하세요."
            }
        ),
        initial=1
    )
    goal_negotiate=forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'name':'goal_negotiate',
            })
    )
    descript=forms.Textarea()

    class Meta:
        model=Project
        fields=['title','budget','budget_show','expired_date','expired_negotiate','goal','goal_negotiate','descript',]

