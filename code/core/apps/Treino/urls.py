from django.urls import path
from . import views

urlpatterns = [
    path('criarTreino', views.criarTreino, name='criarTreino'),
    path('listarTreinos', views.listarTreinos, name='listarTreinos'),
    path('editarTreino/<int:treino_id>', views.editarTreino, name='editarTreino'),
    path('deletarTreino/<int:treino_id>', views.deletarTreino, name='deletarTreino'),
    path('visualizarTreino/<int:treino_id>', views.visualizarTreino, name='visualizarTreino'),
    path('listarTreinoPorUsuario', views.listarTreinoPorUsuario, name='listarTreinoPorUsuario'),

]