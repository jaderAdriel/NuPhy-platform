from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def criarConsulta(request):
    return HttpResponse("criarConsulta")

def editarConsulta(request):
    return HttpResponse("editarConsulta")

def deletarConsulta(request):
    return HttpResponse("deletarConsulta")

def vizualizarConsulta(request):
    return HttpResponse("vizualizarConsulta")

def listarConsultasPorUsuario(request):
    return HttpResponse("listarConsultasPorUsuario")