from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .decorators import admin_required,teamlead_required,teamlead_or_admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test






@admin_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectAddForm(request.POST)
        if form.is_valid():
            p=form.save(commit=False)
            p.added_by=request.user
            p.save()
            messages.success(request,'Project added')
            return redirect('home')
        else:
            messages.error(request,form.errors)
    else:
        form = ProjectAddForm()
    return render(request,'add_project.html',{'form':form})

@admin_required
def add_task(request):
    if request.method == "POST":
        if request.user.is_admin:
            form = AdminTaskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:project_task')
    else:
        form = AdminTaskform()
    return render(request,'task.html',{'form':form})

@admin_required
def edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskEditForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('admins:project_task')
    else:
        form = TaskEditForm(instance=task)
    return render(request,'edittask.html',{'form':form})

@admin_required
def project_task(request):
   if request.method =='POST':
       search=request.POST['search']
       if Project.objects.filter(name__icontains=search).exists():
           tasks=Task.objects.filter(project__in=Project.objects.filter(name__icontains=search))
           return render(request,'view_task.html',{'tasks':tasks})
       else:
           messages.error(request,'Not found !!!')
   else:
       task=Task.objects.all()
   return render(request,'view_task.html',{'tasks':task})

@admin_required
def employee(request):
    userss=User.objects.exclude(is_admin=True)
    user=Profile.objects.filter(user__in=userss)
    return render(request,'employee.html',{'users':user})
