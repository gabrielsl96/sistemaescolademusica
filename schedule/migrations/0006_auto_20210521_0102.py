# Generated by Django 3.2.3 on 2021-05-21 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_auto_20210520_1839'),
        ('schedule', '0005_rename_students_presente_groupclass_students_presents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualclass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persons.student', verbose_name='Aluno(a)'),
        ),
        migrations.AlterField(
            model_name='individualclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persons.teacher', verbose_name='Professor'),
        ),
    ]