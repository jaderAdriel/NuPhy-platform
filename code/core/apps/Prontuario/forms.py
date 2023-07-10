from Horario.models import Horario
from django import forms
from .models import Prontuario



class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = '__all__'
        widgets = {
            'observacoes': forms.Textarea(),
            'consulta': forms.HiddenInput(),
        }
