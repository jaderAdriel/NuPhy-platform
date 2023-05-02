from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def criarHorario(request):
    return HttpResponse("criarHorario")

def editarHorario(request):
    return HttpResponse("editarHorario")

def deletarHorario(request):
    return HttpResponse("deletarHorario")

def listarHorariosPorUsuario(request):
    return HttpResponse("listarHorariosPorUsuario")