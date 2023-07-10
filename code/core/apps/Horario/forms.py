from Horario.models import Horario
from django import forms

class horarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['profissional']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.DateInput(attrs={'type': 'time'}),
        }
        
class horarioModForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'