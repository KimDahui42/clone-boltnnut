# Generated by Django 4.1 on 2022-09-07 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boltnnut', '0004_alter_partners_id_alter_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='expired_negotiation',
            new_name='expired_negotiate',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='goal_negotiation',
            new_name='goal_negotiate',
        ),
    ]