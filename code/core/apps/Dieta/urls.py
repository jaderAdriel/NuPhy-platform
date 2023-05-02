from django.urls import path
from . import views

urlpatterns = [
    path('criarDieta', views.criarDieta, name='criarDieta'),
    path('editarDieta', views.editarDieta, name='editarDieta'),
    path('deletarDieta', views.deletarDieta, name='deletarDieta'),
    path('detalharDieta', views.detalharDieta, name='detalharDieta'),
    path('listarDietaPorUsuario', views.listarDietaPorUsuario, name='listarDietaPorUsuario'),
]