# Generated by Django 3.2 on 2021-05-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20210518_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupclass',
            name='students_presente',
        ),
        migrations.AddField(
            model_name='groupclass',
            name='students_presente',
            field=models.CharField(default=1, max_length=100, verbose_name='Alunos presentes'),
            preserve_default=False,
        ),
    ]
