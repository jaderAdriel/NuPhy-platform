from Horario.models import Horario
from django import forms
from .models import Consulta, Prontuario

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('horario',)
        widgets = {
            'horario': forms.HiddenInput(),
        }

class consultaModForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'