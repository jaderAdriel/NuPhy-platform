from Consulta.models import Consulta
from accounts.models import Usuario
from Horario.models import Horario
from Prontuario.forms import ProntuarioForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Dieta.forms import dietaForm
from Dieta.models import Dieta
from Treino.forms import treinoForm
from Treino.models import Treino
from core.decorators import educador_required, nutri_required, profissional_required, owner_required

# Create your views here.

@login_required
def criarConsulta(request):
    if request.method == "POST":
        id_horario = request.POST.get('horario')
        id_usuario = request.user.id
        horario = get_object_or_404(Horario, id=id_horario)
        paciente = Usuario.objects.get(pk=id_usuario)
        
        Consulta.objects.create(horario=horario, paciente=paciente)

        horario.preenchido = True
        horario.save()
    
    return redirect("/consulta/listarConsultas/")


@login_required
@profissional_required
def deletarConsulta(request, consulta_id):
    
    Consulta.objects.get(pk=consulta_id).delete()
    
    return HttpResponseRedirect("/")


    
@login_required
@profissional_required
def gerenciarConsulta(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    
    profissional = Usuario.objects.get(pk=request.user.id)
    if profissional.tipo == 'N':
        formPlanoDeTrabalho = dietaForm(initial={'consulta': consulta.id})
    else:
        formPlanoDeTrabalho = treinoForm(initial={'consulta': consulta.id})

    context = {
        "consulta": consulta,
        "tipo": profissional.tipo,
        "formProntuario": ProntuarioForm(initial={'consulta': consulta}),
        "formPlanoDeTrabalho" : formPlanoDeTrabalho,
    }

    return render(request, 'consulta/profissionalGerenciarConsulta.html', context)


@login_required
def detalharConsulta(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    
    context = {
        "consulta": consulta,
        "tipo": consulta.horario.profissional.tipo
    }
    
    return render(request, 'consulta/ClienteVizualizaConsulta.html', context)


@login_required
def listarConsulta(request):
    id_usuario = request.user.id
    consultas = []
    usuario = Usuario.objects.get(id=id_usuario) 

    if usuario.tipo == 'N' or usuario.tipo == 'EF' :
        consultas = Consulta.objects.filter(horario__profissional=id_usuario)
    else:
        consultas = Consulta.objects.filter(paciente=id_usuario)

    context = {
        "tipo" : usuario.tipo,
        "consultas": consultas
    }

    if request.method == 'GET':
     
        for campo in request.GET:
            valor = request.GET.get(campo)
            context[campo] = ''
            if valor:
                context[campo] = valor
                filtro = {campo + '__icontains': valor}
                consultas = consultas.filter(**filtro)
    
    context['consultas'] = consultas

    return render(request, 'consulta/index.html', context)



def pesquisar(request):
   
    profissionais = Usuario.objects.exclude(id=request.user.id).filter(tipo__in=['N', 'EF'])

    context = {
        'profissionais': profissionais,
        'user': request.user,
    }

    if request.method == 'GET':
     # Definir os campos de filtro desejados
        campos_filtro = ['tipo', 'cpf', 'codigoAutenticador', 'localAtendimento']
        
        # Aplicar filtros
        for campo in campos_filtro:
            valor = request.GET.get(campo)
            context[campo] = ''
            if valor:
                context[campo] = valor
                filtro = {campo + '__icontains': valor}
                profissionais = profissionais.filter(**filtro)
    
    context['profissionais'] = profissionais

    return render(request, 'consulta/procurar.html', context)