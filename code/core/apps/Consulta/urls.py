from django.urls import path
from . import views

urlpatterns = [
    path('criarConsulta', views.criarConsulta, name='criarConsulta'),
    path('editarConsulta', views.editarConsulta, name='editarConsulta'),
    path('deletarConsulta', views.deletarConsulta, name='deletarConsulta'),
    path('vizualizarConsulta', views.vizualizarConsulta, name='vizualizarConsulta'),
    path('listarConsultasPorUsuario', views.listarConsultasPorUsuario, name='listarConsultasPorUsuario'),

]