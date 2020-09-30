from django.utils.translation import gettext as _


class RoleUser(object):
    Manager = 0
    Employee = 1

    CHOICES = (
        (Manager, _('Менеджер')),
        (Employee, _('Сотрудник')),
    )
