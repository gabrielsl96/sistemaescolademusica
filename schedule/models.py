from django.db import models
from django.db.models.deletion import PROTECT
from persons import models as m

class IndividualClass(models.Model):
	date = models.DateField("Data aula", auto_now=True)
	student = models.OneToOneField(m.Student, on_delete=PROTECT,
		verbose_name="Aluno(a)")
	theme = models.CharField("Tema da aula", max_length=100)
	teacher = models.OneToOneField(m.Teacher, on_delete=PROTECT,
		verbose_name="Professor")
	def __str__(self):
		return str(self.date)+ " | Aluno:" + str(self.student)


class GroupClass(models.Model):
	date = models.DateField(verbose_name="Data aula", auto_now=True)
	group = models.OneToOneField(m.Class, on_delete=PROTECT,
		verbose_name="Turma")
	theme = models.CharField("Tema da aula", max_length=100)
	teacher = models.OneToOneField(m.Teacher, on_delete=PROTECT,
		verbose_name="Professor(a)")
	students_presents = models.CharField(verbose_name="Alunos presentes",
		max_length=100)

	def __str__(self):
		return str(self.date)+ " | Turma:" + str(self.group)
