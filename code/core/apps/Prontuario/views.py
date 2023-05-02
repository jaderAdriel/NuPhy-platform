from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def criarProntuario(request):
    return HttpResponse("criarProntuario")

def editarProntuario(request):
    return HttpResponse("editarProntuario")

def deletarProntuario(request):
    return HttpResponse("deletarProntuario")

def visualizarProntuario(request):
    return HttpResponse("visualizarProntuario")

def listarProntuarioPorConsulta(request):
    return HttpResponse("listarProntuarioPorConsulta")