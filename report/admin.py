from django.contrib import admin
from django.contrib.auth.models import Group
from . models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Employee Details', {'fields': ('is_employee','is_admin','is_teamlead',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Employee Details', {'fields': ('is_employee','is_admin','is_teamlead',)}),
    )
    list_display = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Profile)
admin.site.unregister(Group)
