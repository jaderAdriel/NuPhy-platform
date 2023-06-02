from Treino.models import Treino
from Treino.forms import treinoForm, treinoModForm
from accounts.models import Usuario
from core.decorators import educador_required, nutri_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.

@educador_required
def criarTreino(request):

    if request.method == "POST":
        form = treinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            profissional_id = request.user.id
            profissional = get_object_or_404(Usuario, id=profissional_id)
            treino.profissional = profissional
            treino.save()
            return HttpResponseRedirect("/")
    else:
        form = treinoForm()
    
    context ={
        'form': form
    }
    
    return render(request, "treino/formCriar.html", context)


def listarTreinos(request):
    treino = Treino.objects.all()

    context = {
        "treino": treino
    }
    return render(request, 'treino/listartodos.html', context)

def editarTreino(request, treino_id):
    treino = Treino.objects.get(pk=treino_id)
    
    if request.method == "POST":
        form = treinoModForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = treinoModForm(instance=treino)
    
    context ={
        'form': form,
        'treino_id': treino_id
    }
    
    return render(request, "treino/formEditar.html", context)

def deletarTreino(request, treino_id):
    Treino.objects.get(pk=treino_id).delete()
    
    return HttpResponseRedirect("/")

def visualizarTreino(request, treino_id):
    treino = Treino.objects.filter(id=treino_id)

    context = {
        "treino": treino
    }
    return render(request, 'treino/detalhar.html', context)

def listarTreinoPorUsuario(request):
    dono = request.user.id
    treino = Treino.objects.filter(paciente=dono)

    context = {
        "treino": treino
    }
    return render(request, 'treino/listar.html', context)