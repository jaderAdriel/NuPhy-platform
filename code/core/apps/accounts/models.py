from django.contrib.auth.models import  User
from django.db import models
from core.validators import validate_cpf


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

    
    


# maicon -> jdr2003@
# klebs -> @Admin123
