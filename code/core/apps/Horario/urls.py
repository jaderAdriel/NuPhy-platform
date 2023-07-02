from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerenciarHorario, name='gerenciarHorario'),
    path('criarHorario', views.criarHorario, name='criarHorario'),
    # path('editarHorario/<int:horario_id>', view/s.editarHorario, name='editarHorario'),
    path('deletarHorario/<int:horario_id>/', views.deletarHorario, name='deletarHorario'),
    path('listarHorariosPorUsuario', views.listarHorariosPorUsuario, name='listarHorariosPorUsuario'),

]