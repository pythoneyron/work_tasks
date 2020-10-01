# -*- coding:utf-8 -*-
from django.urls import path

from apps.accounts.views import LoginUserView, LogoutFormView
from apps.accounts.decorators import login_required, manager_rights, employee_rights
from apps.accounts.views import UserListView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('', manager_rights(UserListView.as_view()), name='accounts'),
]
