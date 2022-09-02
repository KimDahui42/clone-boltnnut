# Generated by Django 4.1 on 2022-09-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boltnnut', '0002_project_budget_project_budget_show_project_descript_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='익명', max_length=100)),
                ('describe', models.TextField(null=True)),
                ('address', models.CharField(default='정보 없음', max_length=400)),
                ('site', models.CharField(default='정보 없음', max_length=400)),
                ('category', models.CharField(default='전자/반도체 부품', max_length=20)),
                ('thumbnail', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
