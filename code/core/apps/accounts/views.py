from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.models import Usuario
from .forms import RegistroUsuarioForm
from .permissions import set_permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib import messages

def cadastrar(request):
    
    form = RegistroUsuarioForm()
    
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            
            usuario = form.save(commit=False)
            print(form.cleaned_data)

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
    return render(request, 'registration/profile.html')


@login_required
@user_passes_test(lambda user: user.is_staff)
def listarUsuariosPendentes(request):

    context = {
        'usuarios': Usuario.objects.filter(is_active=False)
    }

    return render(request, 'admin/autorizar-usuarios.html', context=context)


@login_required
@user_passes_test(lambda user: user.is_staff)
def deletarUsuario(request, id):
    # Lógica para deletar o usuário
    Usuario.objects.get(pk=id).delete()

    # Armazena uma mensagem de redirecionamento
    messages.success(request, 'Usuário deletado com sucesso.')

    # Redireciona para a página anterior
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
@user_passes_test(lambda user: user.is_staff)
def autorizarUsuario(request, id):
    # Autorização do usuario
    usuario = Usuario.objects.get(pk=id)
    usuario.is_active = True
    usuario.save()


    # Armazena uma mensagem de redirecionamento
    messages.success(request, 'Usuário autorizado com sucesso.')

    # Redireciona para a página anterior
    return redirect(request.META.get('HTTP_REFERER'))