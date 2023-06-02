from accounts.models import Usuario
from django.db import models

# Create your models here.

class Horario( models.Model ):
    
    dia = models.DateField(help_text="Insira uma data para agenda")

    AGENDA = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )

    agenda = models.CharField(max_length=14, choices=AGENDA)

    profissional = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='professionalH',
    )

    def __str__(self):
        return f'{self.dia.strftime("%d %m %Y")} - {self.profissional}'