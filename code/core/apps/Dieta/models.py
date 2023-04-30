from django.db import models
from accounts.models import Usuario
# Create your models here.

class Dieta( models.Model ):
    
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

    paciente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='pacienteD',
    )

    profissional = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='professionalD',
    )