from rest_framework import serializers
from store.models import Employee, Client, Provider, Category, Product, Order, Sale, SaleDetail

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'