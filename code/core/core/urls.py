from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("accounts.urls")),
    path('treino/', include("Treino.urls")),
    path('prontuario/', include("Prontuario.urls")),
    path('horario/', include("Horario.urls")),
    path('consulta/', include("Consulta.urls")),
    path('dieta/', include("Dieta.urls")),
]
