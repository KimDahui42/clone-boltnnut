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
