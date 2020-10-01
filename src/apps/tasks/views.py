from django.views.generic import ListView, DetailView

from apps.tasks.models import Task


class TasksListView(ListView):
    model = Task
    template_name = 'tasks/list_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self, **kwargs):
        self.queryset = super(TasksListView, self).get_queryset()
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(assigned=user)
        return self.queryset.none()
