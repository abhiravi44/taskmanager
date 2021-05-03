from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .decorators import admin_required,teamlead_required,teamlead_or_admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
def signin(request):
    if request.method =='POST':
        form = LoginForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)
            messages.error(request,'Invalid credentials !!!')
            return redirect('user_reg')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form })


@login_required
def home(request):
    if request.user.is_employee:
        total_tasks=Task.objects.filter(assigned_to=Profile.objects.get(user=request.user)).count()
        task_pending=Task.objects.filter(assigned_to=Profile.objects.get(user=request.user),status='NC').count()
        tasks_completed=Task.objects.filter(assigned_to=Profile.objects.get(user=request.user),status='C').count()
        context={
                 'total_tasks':total_tasks,
                 'tasks_completed':tasks_completed,
                 'task_pending':task_pending,
              }
    if request.user.is_teamlead:
        total_tasks=Task.objects.filter(added_by=request.user).count()
        task_pending=Task.objects.filter(added_by=request.user,status='NC').count()
        tasks_completed=Task.objects.filter(added_by=request.user,status='C').count()
        context={
                 'total_tasks':total_tasks,
                 'tasks_completed':tasks_completed,
                 'task_pending':task_pending,
              }
    if request.user.is_admin:
        team=Team.objects.all()
        context={'team':team}
    return render(request,'home.html',context)


def user_reg(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            messages.error(request,form.errors)
    else:
        form=UserForm()
    return render(request,'reg.html',{'form':form})






@login_required
def project_task(request):
   if request.method =='POST':
       search=request.POST['search']
       if Project.objects.filter(name__icontains=search).exists():
           tasks=Task.objects.filter(project__in=Project.objects.filter(name__icontains=search))
           return render(request,'view_task.html',{'tasks':tasks})
       else:
           messages.error(request,'Not found !!!')
   else:
       task=Task.objects.filter(assigned_to=Profile.objects.get(user=request.user))
   return render(request,'view_task.html',{'tasks':task})




@login_required
def emp_edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == "POST":
        form=EmpTaskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Added')
            return redirect('employee:project_task')
    else:
        form=EmpTaskform(instance=task)
    return render(request,'emp_edit.html',{'form':form})
