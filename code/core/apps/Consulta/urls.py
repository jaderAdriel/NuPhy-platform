from django.urls import path
from . import views

urlpatterns = [
    path('criarConsulta/', views.criarConsulta, name='criar_consulta'),
    path('deletarConsulta/<int:consulta_id>/', views.deletarConsulta, name='deletar_consulta'),
    path('detalhar/<int:consulta_id>/', views.detalharConsulta, name='detalhar_consulta'),
    path('listarConsultas/', views.listarConsulta, name='listar_consultas'),
    path('profissionalGerenciarConsulta/<int:consulta_id>/', views.gerenciarConsulta, name='profissional_gerenciar_consulta'),
    path('procurar_profissional/', views.pesquisar, name='procurar_profissional'),
]
