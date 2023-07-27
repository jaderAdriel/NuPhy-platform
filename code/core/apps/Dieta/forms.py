from Dieta.models import Dieta
from django import forms

class dietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'
        widgets = {
            'consulta': forms.HiddenInput(),
        }
        
class dietaModForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'