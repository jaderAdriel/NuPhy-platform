from django.urls import path
from . import views

urlpatterns = [
    path('criarProntuario', views.criarProntuario, name='criarProntuario'),
    path('editarProntuario', views.editarProntuario, name='editarProntuario'),
    path('deletarProntuario', views.deletarProntuario, name='deletarProntuario'),
]