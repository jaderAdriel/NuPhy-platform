from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('listar', views.listarUsuariosPendentes, name='listar_usuarios_pendentes'),
    path('autorizarUsuario/<int:id>/', views.autorizarUsuario, name='autorizarUsuario'),
    path('deletarUsuario/<int:id>/', views.deletarUsuario, name='deletarUsuario'),
    path('', views.profile, name='profile'),
]