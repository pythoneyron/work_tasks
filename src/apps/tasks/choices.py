from django.utils.translation import gettext as _


class Status(object):
    in_work = 0
    closes = 1
    new = 2

    CHOICES = (
        (in_work, _('В работе (назначена)')),
        (closes, _('Закрыто')),
        (new, _('Создано (запланирована)')),
    )
