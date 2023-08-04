from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.models import Usuario
from .forms import RegistroUsuarioForm, editarAdminForm, editarClienteForm, editarProfissionalForm
from .permissions import set_permissions
from django.contrib.auth.decorators import login_required
from core.decorators import admin_required

from django.shortcuts import redirect
from django.contrib import messages

def cadastrar(request):
    
    form = RegistroUsuarioForm()
    
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            
            usuario = form.save(commit=False)

            if usuario.tipo != "C": 
                usuario.is_active = False

            usuario.save()
            usuario = set_permissions(usuario)

            return redirect('/accounts/login/')
    
    context = {
        'form' : form 
    }

    return render(request, 'registration/registrar.html', context)


@login_required
def profile(request):
    user = Usuario.objects.get(pk=request.user.id)
    form = ''
    if user.tipo == 'C' or user.tipo == 'A':
        form = editarClienteForm(instance=user )
    else:
        form = editarProfissionalForm(instance=user )
            
    context = {
        'usuario' : user,
        'form' : form
    }
    return render(request, 'registration/profile.html', context=context)

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        user = Usuario.objects.get(pk=request.user.id)
        foto_perfil = request.FILES.get('foto')
        form = ''

        if user.tipo == 'C' or user.tipo == 'A':
            form = editarClienteForm(request.POST, instance=user )
        else:
            form = editarProfissionalForm(request.POST, instance=user )

        if foto_perfil:
            user.foto = foto_perfil
            
        if form.is_valid():
            form.save()

    return redirect('/accounts/')

@login_required
@admin_required
def listarUsuariosPendentes(request):

    context = {
        'usuarios': Usuario.objects.filter(is_active=False)
    }

    return render(request, 'admin/autorizar-usuarios.html', context=context)

@login_required
@admin_required
def deletarUsuario(request, id):
    Usuario.objects.get(pk=id).delete()
    messages.success(request, 'Usuário deletado com sucesso.')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
@admin_required
def autorizarUsuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.is_active = True
    usuario.save()

    messages.success(request, 'Usuário autorizado com sucesso.')
    return redirect(request.META.get('HTTP_REFERER'))