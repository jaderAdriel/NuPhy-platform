from django.shortcuts import render, redirect
from accounts.models import Usuario

def solicitar_cadastro(request):
      
    # if request.method == "POST":
    #     form_solicitacao = UsuarioForm(request.POST)
        
    #     if form_solicitacao.is_valid():
    #         usuario = form_solicitacao.save(commit=False)
            
    #         usuario.is_active = False
    #         usuario.save()
            
    #         usuario = set_permission(usuario)
                        
    #         context={
    #             'form_solicitacao': form_solicitacao
    #         }
            
    
    # form_solicitacao = UsuarioForm()
        
    
    return render(request, 'accounts/register.html')
