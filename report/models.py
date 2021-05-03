from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employee=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_teamlead=models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Team(models.Model):
    team=models.CharField(max_length=50,null=True,blank=True)
    members=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.team

    def total_tasks(self):
        task_count=Task.objects.filter(team=Team.objects.get(team=self.team)).count()
        return task_count

    def total_tasks_completed(self):
        tasks_c=Task.objects.filter(team=Team.objects.get(team=self.team),status='C').count()
        return tasks_c

    def total_tasks_notcompleted(self):
        tasks_nc=Task.objects.filter(team=Team.objects.get(team=self.team),status='NC').count()
        return tasks_nc

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    emp_id=models.CharField(max_length=20,unique=True)
    image=models.FileField(upload_to='media/',blank=True)
    designation=models.CharField(max_length=50,blank=True)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username



class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=250)
    added_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name +'|'+ self.team.team


class Task(models.Model):
    status_choice=(
        ('C','Completed'),
        ('NC','Not Completed')
    )
    task=models.TextField(max_length=300)
    project=models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    team=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    added_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='added_by')
    assigned_to=models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True,related_name='assigned_to')
    due_date=models.DateField(null=True)
    status=models.CharField(max_length=50,choices=status_choice,default='NC')
    hours=models.IntegerField(null=True,blank=True)
    comments=models.TextField(max_length=250,null=True,blank=True)



    def __str__(self):
        return self.task[:20]

    def shorten(self):
        return self.task[:20]
