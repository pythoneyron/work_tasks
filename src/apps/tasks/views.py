from django.views.generic import ListView, DetailView

from apps.tasks.models import Task


class TasksListView(ListView):
    model = Task
    template_name = 'tasks/list_tasks.html'
    context_object_name = 'tasks'
