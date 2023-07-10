from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerenciarHorario, name='gerenciarHorario'),
    path('criarHorario', views.criarHorario, name='criarHorario'),
    path('deletarHorario/<int:obj_id>/', views.deletarHorario, name='deletarHorario'),
    path('detalharPerfilProfissional/<int:id>/', views.verPerfilProfissional, name='detalhar_perfil')

]