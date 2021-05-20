from django.shortcuts import render
from courses import views as v
from django.views import View
from django.http import JsonResponse, request

class ViewCourse(View):
	def get(self, request, id_course):
		return (v.get(id_course))

	def post(self, request):
		return (v.post(request))

	def put(self, request, id_course):
		return (v.put(request, id_course))

	def delete(self, request, id_course):
		return (v.delete(request, id_course))
