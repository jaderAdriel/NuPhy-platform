from Dieta.models import Dieta
from django import forms

class dietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'
        
class dietaModForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'