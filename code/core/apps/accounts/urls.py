from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/solicitar/', views.solicitar_cadastro, name='solicitar_cadastro'),
]