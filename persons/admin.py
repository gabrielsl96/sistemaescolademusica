from django.contrib import admin
from django.db.models.base import ModelState
from persons import models

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('name', 'id_p',)
	ordering = ('name', )

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'teacher_display')
	ordering = ('name',)

	def teacher_display(self, obj):
		return ", ".join([teacher.name for teacher in obj.teacher.filter()])
	teacher_display.short_description = "Professor(a)"

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
	list_display = ('id_display', 'course', 'especification', 'teacher',
		'students_display',)

	def students_display(self, obj):
		return ",".join([student.name for student in obj.student.filter()])

	def id_display(self, obj):
		return obj.id

	students_display.short_description = "Alunos"
	id_display.short_description = "Número da Turma"
