from django.db import models
from accounts.models import Usuario

# Create your models here.

class Consulta( models.Model ):
    
    situacao = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('Disponível','D'),
            ('Indisponível','I'),
        ]
    )

    dataHoraComeco = models.DateTimeField()

    dataHoraFinal = models.DateTimeField()

    paciente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='pacienteC',
    )

    profissional = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='professionalC',
    )