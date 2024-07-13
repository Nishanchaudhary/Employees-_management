from django.shortcuts import render,redirect
from .models import Employee 
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from datetime import datetime
from .models import Customer

# Create your views here.
@login_required(login_url='log_in')
def index(request):
    return render(request,"index.html")

@login_required(login_url='log_in')
def add_task(request):
    if request.method=='POST':
        name = request.POST.get('name')
        project_name = request.POST.get('project_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        s_date = request.POST.get('s_date')
        l_date = request.POST.get('l_date')
        Employee.objects.create(name=name,project_name=project_name,email=email,phone=phone,s_date=s_date,l_date=l_date)
        messages.success(request,f"{name} successfully register !!")
        return redirect("add_task")
    return render(request,'add_task.html')

@login_required(login_url='log_in')
def viewtask(request):
    data =  Employee.objects.filter(Isdelete=False)
    return render(request,'viewtask.html',{'data':data})

@login_required(login_url='log_in')
def contact(request):
    date=datetime.now().year
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Customer.objects.create(name=name,email=email,message=message)

        subject="Task management system"
        message=render_to_string('msg.html',{'name':name,'date':date})
        from_email='nishanads77@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        messages.success(request,f"{name} successfully register check your mail!!!")

        return redirect("contact")
     
    return render(request,'contact.html')

@login_required(login_url='log_in')
def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already exists!!!')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is alredy exists")
                return redirect('register')
            else: 
                User.objects.create_user(first_name=name,username=username,email=email,password=password)
                messages.success(request,"Successfully register !!!")
                return redirect('log_in')
        else:
            messages.error(request,"Password doesnot match!!!")
            return redirect('register')
    return render(request,'register.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'username is not found')
            return redirect('log_in')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'log_in.html')

def log_out(request):
    logout(request)
    return redirect('log_in')


def search_form(request):
    if request.method=='POST':
        searched=request.POST['searched']
        finds=Employee.objects.filter(Q(name__icontains=searched) | Q(phone__exact=searched) | Q(email__exact=searched))
    return render(request,'search.html',{'finds':finds})

def delete_data(request,id):
    Emp = Employee.objects.get(id=id)
    Emp.Isdelete = True
    Emp.save()
    return redirect('viewtask')

def update(request,id):
    data = Employee.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        project_name = request.POST.get('project_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        s_date = request.POST.get('s_date')
        l_date = request.POST.get('l_date')
        Emp = Employee.objects.get(id=id)
        Emp.name=name
        Emp.project_name=project_name
        Emp.email=email
        Emp.phone=phone
        Emp.s_date=s_date
        Emp.l_date=l_date
        Emp.save()
        messages.success(request,f'{name} successfully update!!')
        return redirect('viewtask')
    return render(request,'update.html',{'data':data})