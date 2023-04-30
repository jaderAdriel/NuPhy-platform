from django.db import models

# Create your models here.

class Horario( models.Model ):
    
    horarioComeco = models.DateTimeField()

    horarioFim = models.DateTimeField()