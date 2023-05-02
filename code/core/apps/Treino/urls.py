from django.urls import path
from . import views

urlpatterns = [
    path('criarTreino', views.criarTreino, name='criarTreino'),
    path('editarTreino', views.editarTreino, name='editarTreino'),
    path('deletarTreino', views.deletarTreino, name='deletarTreino'),
    path('visualizarTreino', views.visualizarTreino, name='visualizarTreino'),
    path('listarTreinoPorUsuario', views.listarTreinoPorUsuario, name='listarTreinoPorUsuario'),

]