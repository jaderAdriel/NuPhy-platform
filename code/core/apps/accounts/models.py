from django.contrib.auth.models import  User
from django.db import models
from core.validators import validate_cpf

import os
import uuid

def gerar_nome_unico(instance, filename):
    # Obter a extensão do arquivo a partir do nome original
    extensao = filename.split('.')[-1]
    # Gerar um nome único usando UUID4 e a extensão do arquivo
    nome_unico = f"{uuid.uuid4().hex}.{extensao}"
    # Retornar o caminho completo do arquivo
    return os.path.join('fotos_usuarios/', nome_unico)


class Usuario(User):

    ROLE_CHOICES = (
        ("A", "Administrador"),
        ("C", "Cliente"),
        ("N", "Nutricionista"),
        ("EF", "EducadorFisico"),
    )

    codigoAutenticador = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )

    cpf = models.CharField(
        max_length=13,
        unique=True,
        validators=[validate_cpf]
    )

    tipo = models.CharField(
        choices=ROLE_CHOICES,
        blank=False,
        null=False,
        max_length=2
    )

    localAtendimento = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to=gerar_nome_unico,
        blank=True,
        null=True
    )

    
    


# maicon -> jdr2003@
# klebs -> @Admin123
