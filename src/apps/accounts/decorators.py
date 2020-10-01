# -*- coding:utf-8 -*-
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from apps.accounts.choices import RoleUser


def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """ Права для авторизированного пользователя """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url='/accounts/login',
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def manager_rights(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """ Права для Менеджера """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.role == RoleUser.Manager,
        login_url='/accounts/login',
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def employee_rights(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """ Права для Сотрудника """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.role in [RoleUser.Manager, RoleUser.Employee],
        login_url='/accounts/login',
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

