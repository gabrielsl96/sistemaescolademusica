from django.db import models
from django.db.models.deletion import PROTECT
from persons import models as m

class IndividualClass(models.Model):
	date = models.DateField("Data aula", auto_now=True)
	student = models.ForeignKey(m.Student, on_delete=PROTECT,
		verbose_name="Aluno(a)")
	theme = models.CharField("Tema da aula", max_length=100)
	teacher = models.ForeignKey(m.Teacher, on_delete=PROTECT,
		verbose_name="Professor")
	def __str__(self):
		return str(self.date)+ " | Aluno:" + str(self.student)

	class Meta:
		db_table = "class_ind"


class GroupClass(models.Model):
	date = models.DateField(verbose_name="Data aula", auto_now=True)
	group = models.ForeignKey(m.Group, on_delete=PROTECT,
		verbose_name="Turma")
	theme = models.CharField("Tema da aula", max_length=100)
	teacher = models.ForeignKey(m.Teacher, on_delete=PROTECT,
		verbose_name="Professor(a)")
	students_presents = models.CharField(verbose_name="Alunos presentes",
		max_length=100)

	def __str__(self):
		return str(self.date)+ " | Turma:" + str(self.group)

	class Meta:
		db_table = "class_group"
