from core.decorators import nutri_required
from Dieta.forms import dietaForm, dietaModForm
from Dieta.models import Dieta
from accounts.models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.

@nutri_required
def criarDieta(request):

    if request.method == "POST":
        form = dietaForm(request.POST)
        if form.is_valid():
            dieta = form.save(commit=False)
            profissional_id = request.user.id
            profissional = get_object_or_404(Usuario, id=profissional_id)
            dieta.profissional = profissional
            dieta.save()
            return HttpResponseRedirect("/")
    else:
        form = dietaForm()
    
    context ={
        'form': form
    }
    
    return render(request, "dieta/formCriar.html", context)


def listarDietas(request):
    dieta = Dieta.objects.all()

    context = {
        "dieta": dieta
    }
    return render(request, 'dieta/listartodos.html', context)


def editarDieta(request, dieta_id):
    dieta = Dieta.objects.get(pk=dieta_id)
    
    if request.method == "POST":
        form = dietaModForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = dietaModForm(instance=dieta)
    
    context ={
        'form': form,
        'dieta_id': dieta_id
    }
    
    return render(request, "dieta/formEditar.html", context)


def deletarDieta(request, dieta_id):
    
    Dieta.objects.get(pk=dieta_id).delete()
    
    return HttpResponseRedirect("/")


def detalharDieta(request, dieta_id):
    dieta = Dieta.objects.filter(id=dieta_id)

    context = {
        "dieta": dieta
    }
    return render(request, 'dieta/detalhar.html', context)


def listarDietaPorUsuario(request):
    dono = request.user.id
    dieta = Dieta.objects.filter(paciente=dono)

    context = {
        "dieta": dieta
    }
    return render(request, 'dieta/listar.html', context)