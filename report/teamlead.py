from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .decorators import teamlead_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


@teamlead_required
def add_task(request):
    if request.method == "POST":
        form = TLTaskform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.added_by=request.user
            print(form.added_by)
            form.save()
            return redirect('teamlead:tl_view_emp_tasks')
    else:
        form = TLTaskform()
    return render(request,'task.html',{'form':form})

@teamlead_required
def edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskEditForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            if request.user.is_admin:
                return redirect('admins:project_task')
            elif request.user.is_teamlead:
                return redirect('teamlead:tl_view_emp_tasks')
    else:
        form = TaskEditForm(instance=task)
    return render(request,'edittask.html',{'form':form})

@teamlead_required
def teamlead_view(request):
    if request.user.is_teamlead:
        user=Profile.objects.filter(team=Profile.objects.get(user=request.user).team)
        return render(request,'employee.html',{'users':user})
    return render(request,'employee.html')

@teamlead_required
def ajax_team_members(request):
    team_id=request.GET.get('team')
    users=Profile.objects.filter(team=Team.objects.get(id=team_id))
    return render(request,'ajax_team.html',{'users':users})

@teamlead_required
def tl_view_emp_tasks(request):
    task=Task.objects.filter(team=Profile.objects.get(user=request.user).team)
    if request.method =='POST':
        search=request.POST['search']
        if Project.objects.filter(name__icontains=search).exists():
            tasks=Task.objects.filter(project__in=Project.objects.filter(name__icontains=search),team=Profile.objects.get(user=request.user).team)
            return render(request,'view_task.html',{'tasks':tasks})
        else:
            messages.error(request,'Not found !!!')
    return render(request,'view_task.html',{'tasks':task})
