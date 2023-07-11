from django.urls import path
from . import views

urlpatterns = [
    path('criarDieta', views.criarDieta, name='criarDieta'),
    path('editar/<int:dieta_id>/', views.editarDieta, name='editarDieta'),
    path('deletar/<int:dieta_id>/', views.deletarDieta, name='deletarDieta'),
    path('detalhar/<int:dieta_id>/', views.detalharDieta, name='detalharDieta'),
]