from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    s_date = models.DateTimeField()
    l_date = models.DateTimeField()
    Isdelete = models.BooleanField(default=False)

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
