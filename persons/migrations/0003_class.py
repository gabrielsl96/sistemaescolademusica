# Generated by Django 3.2 on 2021-05-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_teacher_specialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ManyToManyField(to='persons.Student', verbose_name='Alunos')),
            ],
        ),
    ]