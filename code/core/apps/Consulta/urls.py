from django.urls import path
from . import views

urlpatterns = [
    path('criarConsulta/', views.criarConsulta, name='criarConsulta'),
    path('editarConsulta/<int:consulta_id>/', views.editarConsulta, name='editarConsulta'),
    path('deletarConsulta/<int:consulta_id>/', views.deletarConsulta, name='deletarConsulta'),
    path('vizualizarConsulta/', views.vizualizarConsulta, name='vizualizarConsulta'),
    path('listarConsultasPorUsuario/', views.listarConsultasPorUsuario, name='listarConsultasPorUsuario'),
    path('procurar_profissional/', views.pesquisar, name='procurar'),
]
