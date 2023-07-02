from Horario.models import Horario
from django import forms

class horarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['profissional']
        widgets = {
            'dia': forms.DateInput(attrs={'type': 'date'}),
        }
        
class horarioModForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'