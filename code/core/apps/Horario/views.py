from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from Horario.forms import horarioForm, horarioModForm
from Horario.models import Horario
from accounts.models import Usuario
from core.decorators import educador_required, nutri_required

# Create your views here.

def criarHorario(request):
    if request.method == "POST":
        form = horarioForm(request.POST)
        if form.is_valid():
            horario = form.save(commit=False)
            profissional_id = request.user.id
            profissional = get_object_or_404(Usuario, id=profissional_id)
            horario.profissional = profissional
            horario.save()
            return HttpResponseRedirect("/")
    else:
        form = horarioForm()
    
    context ={
        'form': form
    }
    
    return render(request, "horario/formCriar.html", context)

def editarHorario(request, horario_id):
    horario = Horario.objects.get(pk=horario_id)
    
    if request.method == "POST":
        form = horarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = horarioForm(instance=horario)
    
    context ={
        'form': form,
        'horario_id': horario_id
    }
    
    return render(request, "horario/formEditar.html", context)

def deletarHorario(request, horario_id):
    Horario.objects.get(pk=horario_id).delete()

    return HttpResponseRedirect("/")

def listarHorariosPorUsuario(request):
    dono = request.user.id
    horario = Horario.objects.filter(profissional=dono)

    context = {
        "horario": horario
    }
    return render(request, 'horario/listar.html', context)