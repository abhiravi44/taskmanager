from django.urls import path,include
from report import views,teamlead,admins



urlpatterns=[
    path('admins/',include(([

        path('addtask/',admins.add_task,name='add_task'),
        path('employee/',admins.employee,name='employee'),
        path('addproject/',admins.add_project,name='add_project'),
        path('projecttask/',admins.project_task,name='project_task'),
        path('edit_task/<int:id>/',admins.edit_task,name='edit_task'),
    ],'report'),namespace='admins')),

    path('teamlead/',include(([

        path('teamlead_view/',teamlead.teamlead_view,name='teamlead_view'),
        path('tl_view_emp_tasks/',teamlead.tl_view_emp_tasks,name='tl_view_emp_tasks'),
        path('addtask/',teamlead.add_task,name='add_task'),
        path('edit_task/<int:id>/',teamlead.edit_task,name='edit_task'),
        path('ajax/load_members/',teamlead.ajax_team_members,name='ajax_team_members'),
    ],'report'),namespace='teamlead')),

    path('employee/',include(([
        path('edit_task/<int:id>/',views.emp_edit_task,name='emp_edit_task'),
        path('projecttask/',views.project_task,name='project_task'),
    ],'report'),namespace='employee')),


]
