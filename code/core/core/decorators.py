from django.contrib.auth.decorators import user_passes_test

def educador_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name='Educador Fisico').exists(),
        login_url='/accounts/login/'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def nutri_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name='Nutricionista').exists(),
        login_url='/accounts/login/'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator