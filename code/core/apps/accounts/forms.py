from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "cpf", "tipo", "codigoAutenticador", "email", "username", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        codigo_autenticador = cleaned_data.get('codigoAutenticador')

        if tipo in ('EF', 'N') and not codigo_autenticador:
            self.add_error('codigoAutenticador', 'Campo obrigatório para o tipo selecionado')