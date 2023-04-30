from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario

class RegistroUsuarioForm( UserCreationForm ):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "cpf", "tipo" , "email", "username", "password1", "password2"]