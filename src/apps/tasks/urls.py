# -*- coding:utf-8 -*-
from django.urls import path

from apps.accounts.decorators import login_required, manager_rights, employee_rights
from apps.tasks.views import TasksListView

app_name = 'tasks'

urlpatterns = [
    path('', employee_rights(TasksListView.as_view()), name='tasks'),

]
