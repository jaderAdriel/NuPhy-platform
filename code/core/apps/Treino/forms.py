from Treino.models import Treino
from django import forms

class treinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = '__all__'
        
class treinoModForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = '__all__'
        widgets = {
            'consulta': forms.HiddenInput(),
        }