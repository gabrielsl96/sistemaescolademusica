from django.db import models
from django.db.models.deletion import CASCADE
from courses.models import Course
import uuid

class Teacher(models.Model):
	id_p = models.UUIDField("Id", primary_key=True, editable=False,
		unique=True, default=uuid.uuid4)
	name = models.CharField("Nome", max_length=50)
	email = models.EmailField("E-mail", max_length=50)
	specialty = models.ManyToManyField(Course, verbose_name="Especialidade")

	def __str__(self):
		return str(self.name)

class Student(models.Model):
	id = models.UUIDField("Id", primary_key=True, editable=False,
		unique=True, default=uuid.uuid4)
	name = models.CharField("Nome", max_length=50)
	teacher = models.ManyToManyField(Teacher, verbose_name="Professor(a)")
	course = models.ManyToManyField(Course, verbose_name="Curso(s)")

	def __str__(self):
		return str(self.name)

class Class(models.Model):
	student = models.ManyToManyField(Student, verbose_name="Alunos")
	teacher = models.OneToOneField(Teacher, verbose_name="Professor(a) da turma",
		on_delete=CASCADE)
	course = models.OneToOneField(Course, on_delete=CASCADE,
		verbose_name="Curso")
	especification = models.CharField("Descrição da Turma", max_length=30)

	def __str__(self):
		return str(self.id)

