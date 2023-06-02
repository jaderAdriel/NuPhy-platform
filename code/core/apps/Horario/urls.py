from django.urls import path
from . import views

urlpatterns = [
    path('criarHorario', views.criarHorario, name='criarHorario'),
    path('editarHorario/<int:horario_id>', views.editarHorario, name='editarHorario'),
    path('deletarHorario/<int:horario_id>', views.deletarHorario, name='deletarHorario'),
    path('listarHorariosPorUsuario', views.listarHorariosPorUsuario, name='listarHorariosPorUsuario'),

]