# Generated by Django 4.1 on 2022-09-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boltnnut', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='budget_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='descript',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='expired_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='expired_negotiation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='goal_negotiation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
