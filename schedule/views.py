from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from schedule.models import GroupClass, IndividualClass
from api.serializers import GroupClassSerializer, IndividualClassSerializer

@permission_classes([IsAuthenticated])
class IndividualClassViewSet(viewsets.ModelViewSet):
	queryset = IndividualClass.objects.all()
	serializer_class = IndividualClassSerializer

@permission_classes([IsAuthenticated])
class GroupClassViewSet(viewsets.ModelViewSet):
	queryset = GroupClass.objects.all()
	serializer_class = GroupClassSerializer
