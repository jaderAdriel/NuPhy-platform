from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def criarTreino(request):
    return HttpResponse("criarTreino")

def editarTreino(request):
    return HttpResponse("editarTreino")

def deletarTreino(request):
    return HttpResponse("deletarTreino")

def visualizarTreino(request):
    return HttpResponse("visualizarTreino")

def listarTreinoPorUsuario(request):
    return HttpResponse("listarTreinoPorUsuario")