from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None,redirect=REDIRECT_FIELD_NAME,login_url='/'):
    _decorator=user_passes_test(
    lambda u: u.is_active and u.is_admin,login_url=login_url,redirect_field_name=redirect
    )
    if function:
        return _decorator(function)

    return _decorator

def teamlead_required(function=None,redirect=REDIRECT_FIELD_NAME,login_url='/'):
    _decorator=user_passes_test(
    lambda u: u.is_active and u.is_teamlead,login_url=login_url,redirect_field_name=redirect
    )
    if function:
        return _decorator(function)

    return _decorator

def teamlead_or_admin(function=None,redirect=REDIRECT_FIELD_NAME,login_url='/'):
    _decorator=user_passes_test( lambda u:u.is_admin or  u.is_teamlead,
                                login_url=login_url,
                                redirect_field_name=redirect)
    if function:
        return _decorator(function)
    return _decorator
