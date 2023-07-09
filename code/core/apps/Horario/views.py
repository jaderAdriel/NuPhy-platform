from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from Horario.forms import horarioForm, horarioModForm
from Horario.models import Horario
from accounts.models import Usuario
from core.decorators import educador_required, nutri_required, profissional_required, owner_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

@login_required
@profissional_required
def gerenciarHorario(request):
    horarios = Horario.objects.filter(profissional=request.user)

    context = {
        'horarios': horarios,
        'form': horarioForm(),
    }

    return render(request, "horario/index.html", context)

@login_required
@profissional_required
def criarHorario(request):

    context = {
        'form': horarioForm()
    }

    if request.method == "POST":
        form = horarioForm(request.POST)

        if form.is_valid():
            horario = form.save(commit=False)
            profissional_id = request.user.id
            profissional = get_object_or_404(Usuario, id=profissional_id)
            horario.profissional = profissional
            horario.save()
            messages.success(request, 'Horario adicionado na agenda com sucesso.')
        else:
            messages.error(request, "Não foi possivel criar o horario")

        # Redireciona para a página anterior
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, "horario/index.html", context)


@login_required
@profissional_required
@owner_required(Horario, "profissional_id")
def deletarHorario(request, obj_id):
    Horario.objects.get(pk=obj_id).delete()

    messages.success(request, 'Horario deletado da agenda com sucesso.')

    return redirect(request.META.get('HTTP_REFERER'))
