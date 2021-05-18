from django.db import models

class Course(models.Model):
	name = models.CharField("Curso", max_length=20)

	def __str__(self):
		return str(self.name)
