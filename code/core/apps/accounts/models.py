from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import Group, Permission

from django.db import models
from multiselectfield import MultiSelectField

from core.validators import validate_cpf


class Usuario(AbstractUser):

    ROLE_CHOICES = (
        ("A", "Administrador"),
        ("C", "Cliente"),
        ("P", "Profissional"),
    )

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios',
        blank=True,
        help_text='Os grupos aos quais este usuário pertence. '
                  'Um usuário com acesso a um grupo terá todas as permissões '
                  'atribuídas a esse grupo.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios',
        blank=True,
        help_text='Especifica as permissões específicas do usuário. '
                  'Isso é usado em conjunto com as permissões de grupo.'
    )

    codigoAutenticador = models

    cpf = models.CharField(
        max_length=13,
        primary_key=True,
        validators=[validate_cpf]
    )

    tipo = MultiSelectField(
        choices=ROLE_CHOICES,
        max_length=20,
        max_choices=1,
    )

    localAtendimento = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.username = self.cpf
        super(Usuario, self).save(*args, **kwargs)