from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("accounts.urls")),
    path('treino/', include("Treino.urls")),
    path('prontuario/', include("Prontuario.urls")),
    path('horario/', include("Horario.urls")),
    path('consulta/', include("Consulta.urls")),
    path('dieta/', include("Dieta.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)