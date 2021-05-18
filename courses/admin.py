from django.contrib import admin
from courses import models as m

@admin.register(m.Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)
	ordering = ['-name',]
