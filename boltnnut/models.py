from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,)
    budget=models.IntegerField()
    attached=models.FileField('첨부 파일',upload_to='',blank=True)
    