# Generated by Django 4.1.4 on 2023-01-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_name_role_rname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='rname',
            new_name='r_name',
        ),
    ]