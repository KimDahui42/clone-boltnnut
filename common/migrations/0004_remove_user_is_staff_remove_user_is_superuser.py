# Generated by Django 4.1 on 2022-09-05 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]
