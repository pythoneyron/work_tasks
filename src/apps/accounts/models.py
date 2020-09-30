from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext as _

from apps.accounts.choices import RoleUser


class User(AbstractUser):
    role = models.PositiveIntegerField(verbose_name=_('Роль'), choices=RoleUser.CHOICES, default=RoleUser.Employee)

