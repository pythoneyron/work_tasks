from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, View

from apps.accounts.models import User
from apps.accounts.choices import RoleUser


class LoginUserView(LoginView):
    """ Авторизация """
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request, user)
        if user.role == RoleUser.Manager:
            return redirect('accounts:accounts')
        return redirect('tasks:tasks')


class LogoutFormView(View):
    """ Выход из профиля """
    def get(self, request):
        auth_logout(request)
        return redirect('/')


class UserListView(ListView):
    """Отображение списка пользователей"""
    model = User
    template_name = 'accounts/list_users.html'
    context_object_name = 'users'

