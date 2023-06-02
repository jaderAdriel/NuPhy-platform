from django.urls import path
from . import views

urlpatterns = [
    path('criarDieta', views.criarDieta, name='criarDieta'),
    path('listarDietas', views.listarDietas, name='listarDietas'),
    path('editarDieta/<int:dieta_id>', views.editarDieta, name='editarDieta'),
    path('deletarDieta/<int:dieta_id>', views.deletarDieta, name='deletarDieta'),
    path('detalharDieta/<int:dieta_id>', views.detalharDieta, name='detalharDieta'),
    path('listarDietaPorUsuario', views.listarDietaPorUsuario, name='listarDietaPorUsuario'),
]