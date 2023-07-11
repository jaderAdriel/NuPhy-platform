from django.urls import path
from . import views

urlpatterns = [
    path('criarConsulta/', views.criarConsulta, name='criar_consulta'),
    path('deletarConsulta/<int:consulta_id>/', views.deletarConsulta, name='deletar_consulta'),
    path('detalhar/<int:consulta_id>/', views.detalharConsulta, name='detalhar_consulta'),
    # path('listarConsultaCliente/', views.vizualizarConsulta, name='listar_consulta_cliente'),
    path('listarConsultasProfissional/', views.listarConsultasProfissional, name='listar_consultas_por_profissional'),
    path('listarConsultasCliente/', views.listarConsultasProfissional, name='listar_consultas_por_cliente'),
    path('profissionalGerenciarConsulta/<int:consulta_id>/', views.gerenciarConsulta, name='profissional_gerenciar_consulta'),
    path('procurar_profissional/', views.pesquisar, name='procurar_profissional'),
]
