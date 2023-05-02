from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def criarDieta(request):
    return HttpResponse("criarDieta")

def editarDieta(request):
    return HttpResponse("editarDieta")

def deletarDieta(request):
    return HttpResponse("deletarDieta")

def detalharDieta(request):
    return HttpResponse("detalharDieta")

def listarDietaPorUsuario(request):
    return HttpResponse("listarDietaPorUsuario")