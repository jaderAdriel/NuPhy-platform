from Horario.models import Horario
from django import forms

class horarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        exclude = ['profissional']
        
class horarioModForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'