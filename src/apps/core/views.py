from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.accounts.choices import RoleUser


class Home(TemplateView):
    template_name = 'base.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.role == RoleUser.Manager:
            return redirect('accounts:accounts')

        elif user.role == RoleUser.Employee:
            return redirect('tasks:tasks')
