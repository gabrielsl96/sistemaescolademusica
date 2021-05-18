from django.contrib import admin
from schedule import models

@admin.register(models.IndividualClass)
class IndivClassAdmin(admin.ModelAdmin):
	list_display = ('id', 'date', 'student', 'teacher')

@admin.register(models.GroupClass)
class GroupClassAdmin(admin.ModelAdmin):
	list_display = ('id', 'date', 'group', 'students_presents', 'teacher')
