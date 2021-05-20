from django.shortcuts import render
from courses.models import Course as c
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

def get(name_course):
	try:
		course = c.objects.get(name=name_course)
		data = {
			'id':course.id,
			'name':course.name,
		}
		return JsonResponse(data)
	except ObjectDoesNotExist:
		data = {
			'messsage':"Id inválido ou curso inexistente"
		}
		return JsonResponse(data)

def post(request):
	body_course = json.loads(request.body)
	name_course = body_course.get('name')
	if name_course:
		if not c.objects.filter(name=name_course.capitalize()):
			course_data ={
				'name':name_course.capitalize()
			}
			new_course = c.objects.create(**course_data)
			data = {
				'message': f"Curso {name_course.capitalize()} criado com sucesso! \
				Id:{new_course.id}"
			}
		else:
			data = {
				'message':'Esse curso já existe!'
			}
	else:
		data = {
			'messsage':'Parametro inválido informado'
		}
	return JsonResponse(data)

def put(request, id_course):
	try:
		course = c.objects.get(id=id_course)
		put_body = json.loads(request.body)
		course.name = put_body.get('name')
		course.save()
		data = {
			'message': f"Nome do curso atualizado : {course.name}"
		}
		return JsonResponse(data)
	except ObjectDoesNotExist:
		data = {
				'message': "ID inválido"
			}
		return JsonResponse(data)

def delete(request, id_course):
	try:
		course = c.objects.get(id=id_course)
		course_name = course.name
		course.delete()
		data = {
			'message': f"Curso deleteado : {course_name}"
		}
		return JsonResponse(data)
	except ObjectDoesNotExist:
		data = {
				'message': "ID inválido"
			}
		return JsonResponse(data)
