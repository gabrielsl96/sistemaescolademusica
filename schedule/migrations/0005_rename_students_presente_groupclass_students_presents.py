# Generated by Django 3.2 on 2021-05-18 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210518_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupclass',
            old_name='students_presente',
            new_name='students_presents',
        ),
    ]
