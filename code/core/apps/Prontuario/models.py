from django.db import models
from django.db.models.fields.related import OneToOneField
from Consulta.models import Consulta
from accounts.models import Usuario

# Create your models here.

class Prontuario( models.Model ):
    consulta =  OneToOneField(Consulta, on_delete=models.CASCADE, related_name='prontuario')
    observacoes = models.CharField(
        max_length=2500,
        blank=False,
        null=False
    )