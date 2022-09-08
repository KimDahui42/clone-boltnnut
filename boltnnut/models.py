from pydoc import describe
from tkinter import CASCADE
from django.db import models

from common.models import User

# Create your models here.
class Project(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,null=True)
    budget=models.IntegerField(default=0)
    budget_show=models.BooleanField(default=True)
    expired_date=models.DateField(null=True)
    expired_negotiate=models.BooleanField(default=False)
    goal=models.IntegerField(default=1)
    goal_negotiate=models.BooleanField(default=False)
    descript=models.TextField(null=True)
    ongoing=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    id=models.AutoField(primary_key=True)
    project=models.ForeignKey('Project',on_delete=models.CASCADE)
    file=models.FileField(upload_to='Uploaded Files/')
    
    def __str__(self):
        return self.project

class Partners(models.Model):
    id=models.AutoField(primary_key=True)
    company=models.CharField(max_length=100,default="익명")
    describe=models.TextField(null=True)
    address=models.CharField(max_length=400,default="정보 없음")
    site=models.CharField(max_length=400,default="정보 없음")
    category=models.CharField(max_length=20,default="전자/반도체 부품")
    thumbnail=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.company

