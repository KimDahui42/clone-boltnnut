from pydoc import describe
from django.db import models

from common.models import User

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,null=True)
    budget=models.IntegerField(default=0)
    budget_show=models.BooleanField(default=True)
    expired_date=models.DateField(null=True)
    expired_negotiation=models.BooleanField(default=False)
    goal=models.IntegerField(default=1)
    goal_negotiation=models.BooleanField(default=False)
    descript=models.TextField(null=True)
    attached=models.FileField('첨부 파일',upload_to='',blank=True)

class Partners(models.Model):
    company=models.CharField(max_length=100,default="익명")
    describe=models.TextField(null=True)
    address=models.CharField(max_length=400,default="정보 없음")
    site=models.CharField(max_length=400,default="정보 없음")
    category=models.CharField(max_length=20,default="전자/반도체 부품")
    thumbnail=models.CharField(max_length=200,null=True)


