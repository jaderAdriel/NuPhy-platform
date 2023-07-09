from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from functools import wraps

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

def profissional_required(view_func):
    def test_func(user):
        return user.groups.filter(name='Educador Fisico').exists() or user.groups.filter(name='Nutricionista').exists()

    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'error/403.html', status=403)

        return wrapped_view

    return decorator(view_func)


def owner_required(model_class, field_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            obj = get_object_or_404(model_class, pk=kwargs['obj_id'])
            if getattr(obj, field_name) != request.user.id:
                messages.error(request, 'Você não tem permissão para acessar este objeto.')
                return render(request, 'error/403.html', status=403)

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
