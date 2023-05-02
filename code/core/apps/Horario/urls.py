from django.urls import path
from . import views

urlpatterns = [
    path('criarHorario', views.criarHorario, name='criarHorario'),
    path('editarHorario', views.editarHorario, name='editarHorario'),
    path('deletarHorario', views.deletarHorario, name='deletarHorario'),
    path('listarHorariosPorUsuario', views.listarHorariosPorUsuario, name='listarHorariosPorUsuario'),

]