from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

from crispy_forms.helper import FormHelper

from django.contrib.auth import authenticate

class UserForm(UserCreationForm):
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','is_employee')


    def __init__(self,*args,**kwargs):
        super(UserForm, self).__init__(*args,**kwargs)
        self.fields['username'].required=True
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['email'].required=True
        self.fields['is_employee'].required=True
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class AdminTaskform(forms.ModelForm):
    class Meta():
        model=Task
        fields=('task','project','team','assigned_to','due_date')
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self,*args,**kwargs):
        super(AdminTaskform, self).__init__(*args,**kwargs)
        self.fields['task'].required=True
        self.fields['project'].required=True
        self.fields['team'].required=True
        self.fields['assigned_to'].filter=True
        self.fields['due_date'].required=True

class TLTaskform(forms.ModelForm):
    class Meta():
        model=Task
        fields=('task','team','project','assigned_to','due_date')
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'}),

        }

    def __init__(self,*args,**kwargs):
        super(TLTaskform, self).__init__(*args,**kwargs)
        self.fields['task'].required=True
        self.fields['project'].required=True
        self.fields['team'].required=True
        self.fields['due_date'].required=True
        self.fields['assigned_to'].queryset=Profile.objects.none()

        if 'team' in self.data:
            try:
                team_id=int(self.data.get('team'))
                self.fields['assigned_to'].queryset=Profile.objects.filter(team=Team.objects.get(id=team_id))
            except (ValueError,TypeError):
                pass
        # elif self.instance.pk:
        #     self.fields['assigned_to'].queryset = self.instance.team




class TaskEditForm(forms.ModelForm):
    class Meta():
        model=Task
        fields=('task','project','team','assigned_to','due_date','status','hours','comments')
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self,*args,**kwargs):
        super(TaskEditForm, self).__init__(*args,**kwargs)
        self.fields['task'].required=True
        self.fields['project'].required=True
        self.fields['team'].required=True
        self.fields['assigned_to'].required=True
        self.fields['due_date'].required=True




class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    username = forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','description','team')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Title of project'}),
            'description': forms.TextInput(attrs={'placeholder':'Description'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProjectAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['description'].required = True
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class EmpTaskform(forms.ModelForm):
    class Meta():
        model=Task
        fields=('task','status','hours','comments')

    def __init__(self,*args,**kwargs):
        super(EmpTaskform, self).__init__(*args,**kwargs)
        self.fields['status'].required=True
        self.fields['hours'].required=True
