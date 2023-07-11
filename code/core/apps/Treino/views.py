from Treino.models import Treino
from Treino.forms import treinoForm, treinoModForm
from accounts.models import Usuario
from core.decorators import educador_required, nutri_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

@educador_required
def criarTreino(request):

    if request.method == "POST":
        form = treinoForm(request.POST)
        if form.is_valid():
            treino = form.save()
    
    
    return redirect(request.META.get('HTTP_REFERER'))

##################

def editarTreino(request, treino_id):
    treino = Treino.objects.get(pk=treino_id)
    
    if request.method == "POST":
        form = treinoModForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect(f'/consulta/detalhar/{treino.consulta.id}/')
    else:
        form = treinoModForm(instance=treino)
    
    context ={
        'form': form,
    }
    
    return render(request, "editarPlanoTrabalho.html", context)

##################

def deletarTreino(request, treino_id):
    Treino.objects.get(pk=treino_id).delete()
    
    return redirect(request.META.get('HTTP_REFERER'))


#################

def detalharTreino(request, treino_id):
    treino = Treino.objects.get(pk=treino_id)

    context = {
        "treino": treino
    }
    
    return render(request, 'detalharPlanoTrabalho.html', context)
