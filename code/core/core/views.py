from django.shortcuts import render

def home(request):
    user = request.user

    context = {
        'user': user,
        # Outras variáveis de contexto que você desejar incluir
    }
    return render(request, 'home.html', context)
