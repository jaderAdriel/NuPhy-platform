from django.db import models
from accounts.models import Usuario

# Create your models here.

class Prontuario( models.Model ):
    
    paciente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='pacienteP',
    )

    profissional = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='professionalP',
    )

    data = models.DateTimeField()

    observacoes = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )