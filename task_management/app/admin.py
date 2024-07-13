from django.contrib import admin
from .models import Employee
from .models import Customer
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','project_name','email','phone','s_date','l_date']
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']