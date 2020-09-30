from django.views.generic import ListView, DetailView

from apps.accounts.models import User


class UserListView(ListView):
    model = User
    template_name = 'accounts/list_users.html'
    context_object_name = 'users'

