from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProntuarioForm
# Create your views here.

def criarProntuario(request):
    if request.method == "POST": 
        form = ProntuarioForm(request.POST)

        if form.is_valid():
            form.save()
            
    return redirect(request.META.get('HTTP_REFERER'))

def editarProntuario(request):
    return HttpResponse("editarProntuario")

def deletarProntuario(request):
    return HttpResponse("deletarProntuario")

def visualizarProntuario(request):
    return HttpResponse("visualizarProntuario")

def listarProntuarioPorConsulta(request):
    return HttpResponse("listarProntuarioPorConsulta")