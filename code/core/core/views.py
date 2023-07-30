from django.shortcuts import redirect, render

def home(request):
    if not request.user.is_authenticated: 
        return render(request, 'home.html')

    tipo = request.user.usuario.tipo
    if tipo == 'C':
        return redirect('/consulta/listarConsultas/')
    elif tipo == 'A':
        return redirect('/accounts/listar')
    else:
        return redirect('/horario/')


