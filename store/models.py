from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    provider = models.ForeignKey(Provider, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'PENDING',
        PROCESSING = 'PROCESSING',
        COMPLETED = 'COMPLETED',
        CANCELLED = 'CANCELLED'
    
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    total = models.FloatField()

class Sale(models.Model):
    id = models.AutoField(primary_key=True)\
    # uuid
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    total = models.FloatField()

class SaleDetail(models.Model):
    id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
