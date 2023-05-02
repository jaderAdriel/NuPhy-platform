from django.urls import path
from . import views

urlpatterns = [
    path('criarProntuario', views.criarProntuario, name='criarProntuario'),
    path('editarProntuario', views.editarProntuario, name='editarProntuario'),
    path('deletarProntuario', views.deletarProntuario, name='deletarProntuario'),
    path('visualizarProntuario', views.visualizarProntuario, name='visualizarProntuario'),
    path('listarProntuarioPorConsulta', views.listarProntuarioPorConsulta, name='listarProntuarioPorConsulta'),

]