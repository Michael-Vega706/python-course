from django.http import HttpResponse
from rest_framework import viewsets
from store.models import Employee, Client
from store.serializers import EmployeeSerializer, ClientSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer