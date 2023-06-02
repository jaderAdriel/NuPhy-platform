from django.shortcuts import render, redirect
from accounts.models import Usuario
from .forms import RegistroUsuarioForm
from .permissions import set_permissions

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

def profile(request):
    return render(request, 'registration/profile.html')