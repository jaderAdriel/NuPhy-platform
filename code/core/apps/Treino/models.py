from django.db import models
from accounts.models import Usuario
from Consulta.models import Consulta
# Create your models here.

class Treino( models.Model ):
    
    diaSemana = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('Segunda-feira','SF'),
            ('Terça-feira','TF'),
            ('Quarta-feira','QAF'),
            ('Quinta-feira','QIF'),
            ('Sexta-feira','SF'),
            ('Sábado','S'),
            ('Domingo','D'),
        ]
    )

    exercicio = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    serie = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    repeticao = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.CASCADE,
        related_name='treino',
    )
