from core.decorators import nutri_required
from Dieta.forms import dietaForm, dietaModForm
from Dieta.models import Dieta
from accounts.models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from Consulta.models import Consulta
# Create your views here.

@nutri_required
def criarDieta(request):

    if request.method == "POST":
        form = dietaForm(request.POST)
        if form.is_valid():
            dieta = form.save(commit=False)
            dieta.save()
            return redirect(f'/consulta/detalhar/{dieta.consulta.id}/')
    else:
        form = dietaForm()
    
    context ={
        'form': form
    }
    
    return redirect(request.META.get('HTTP_REFERER'))


def editarDieta(request, dieta_id):
    dieta = Dieta.objects.get(pk=dieta_id)

   

    if request.method == "POST":
        form = dietaForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            return redirect(f'/consulta/detalhar/{dieta.consulta.id}/')
    else:
        form = dietaForm(instance=dieta)

    context ={
        'form': form,
        "dieta": dieta
    }
    
    return render(request, "editarPlanoTrabalho.html", context)


def deletarDieta(request, dieta_id):
    
    dieta = Dieta.objects.get(pk=dieta_id)
    consulta_id = dieta.consulta.id
    dieta.delete()
    
    return redirect(f'/consulta/detalhar/{consulta_id}/')


def detalharDieta(request, dieta_id):
    dieta = Dieta.objects.get(pk=dieta_id)

    context = {
        "dieta": dieta
    }

    return render(request, 'detalharPlanoTrabalho.html', context)


