from accounts.models import Usuario
from django.db import models
from datetime import time
# Create your models here.

class Horario( models.Model ):
    
    data = models.DateField(
        help_text="Insira uma data para agenda",
        blank=False,
        null=False,
    )

    
    hora = models.TimeField(
        blank=False,
        null=False,
        default=time(10, 0)
    )

    preenchido = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    profissional = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='professionalH',
    )
