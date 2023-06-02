from Treino.models import Treino
from django import forms

class treinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        exclude = ['profissional']
        
class treinoModForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = '__all__'