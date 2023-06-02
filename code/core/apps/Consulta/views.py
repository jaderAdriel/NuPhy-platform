from Consulta.models import Consulta
from accounts.models import Usuario
from Consulta.forms import consultaForm, consultaModForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def criarConsulta(request):
    
    if request.method == "POST":
        form = consultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            paciente_id = request.user.id
            paciente = get_object_or_404(Usuario, id=paciente_id)
            consulta.paciente = paciente
            consulta.save()
            return HttpResponseRedirect("/")
    else:
        form = consultaForm()
    
    context ={
        'form': form
    }
    
    return render(request, "consulta/formCriar.html", context)


def editarConsulta(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    
    if request.method == "POST":
        form = consultaModForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = consultaModForm(instance=consulta)
    
    context ={
        'form': form,
        'consulta_id': consulta_id
    }
    
    return render(request, "consulta/formEditar.html", context)

@login_required
def deletarConsulta(request, consulta_id):
    
    Consulta.objects.get(pk=consulta_id).delete()
    
    return HttpResponseRedirect("/")
    

def vizualizarConsulta(request):
    consulta = Consulta.objects.all()

    context = {
        "consulta": consulta
    }
    return render(request, 'consulta/listartodos.html', context)

@login_required
def listarConsultasPorUsuario(request):
    dono = request.user.id
    consulta = Consulta.objects.filter(paciente=dono)

    context = {
        "consulta": consulta
    }
    return render(request, 'consulta/listar.html', context)