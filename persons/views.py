from rest_framework import viewsets, permissions
from api import serializers as s
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from persons.models import Teacher, Student, Group

@permission_classes([IsAuthenticated])
class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = s.TeacherSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@permission_classes([IsAuthenticated])
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = s.StudentSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@permission_classes([IsAuthenticated])
class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = s.GroupSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
