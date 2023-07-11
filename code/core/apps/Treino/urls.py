from django.urls import path
from . import views

urlpatterns = [
    path('criarTreino', views.criarTreino, name='criarTreino'),
    path('editar/<int:treino_id>/', views.editarTreino, name='editarTreino'),
    path('deletar/<int:treino_id>/', views.deletarTreino, name='deletarTreino'),
    path('detalhar/<int:treino_id>/', views.detalharTreino, name='visualizarTreino'),

]