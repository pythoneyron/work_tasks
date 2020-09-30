from django.db import models

from django.utils.translation import gettext as _

from apps.accounts.models import User
from apps.tasks.choices import Status


class Task(models.Model):
    title = models.CharField(verbose_name=_('Заголовок'), max_length=255)
    description = models.TextField(verbose_name=_('Описание'), max_length=1024)
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, blank=True)
    changed = models.DateTimeField(verbose_name=_('Дата редактирования'), blank=True, null=True)
    assigned = models.ManyToManyField(User, verbose_name=_('Назначено'), blank=True, related_name='tasks')
    status = models.PositiveIntegerField(verbose_name=_('Статус'), default=Status.new, choices=Status.CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')
