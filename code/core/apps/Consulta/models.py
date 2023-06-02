from Horario.models import Horario
from django.db.models.fields.related import OneToOneField
from django.db import models
from accounts.models import Usuario


# Create your models here.

class Consulta( models.Model ):
    horario =  OneToOneField(Horario, on_delete=models.CASCADE, related_name='horario')
    
    paciente = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='pacienteC',
    )

    def __str__(self):
        return f'{self.horario} - {self.paciente}'