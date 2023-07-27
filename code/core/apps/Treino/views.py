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
        form = treinoForm(request.POST, instance=treino)
        id_consulta = request.POST.get('consulta')
        form.consulta = id_consulta
        if form.is_valid():
            form.save()
            return redirect(f'/consulta/detalhar/{treino.consulta.id}/')


    context ={
        'form': treinoForm(instance=treino),
        'dieta': treino
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
