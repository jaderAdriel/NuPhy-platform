from django.db import models
from accounts.models import Usuario
# Create your models here.
from Consulta.models import Consulta

class Dieta( models.Model ):
    
    diaSemana = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('SF','Segunda-feira'),
            ('TF','Terça-feira'),
            ('QAF','Quarta-feira'),
            ('QIF','Quinta-feira'),
            ('SF','Sexta-feira'),
            ('S','Sábado'),
            ('D','Domingo'),
        ]
    )

    quantidade = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    alimento = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    horario = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.CASCADE,
        related_name='dieta',
    )
