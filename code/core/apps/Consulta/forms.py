from Horario.models import Horario
from django import forms
from .models import Consulta

class consultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['horario',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = Horario.objects.exclude(horario__isnull=False)
        self.fields['horario'].queryset = queryset

class consultaModForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'