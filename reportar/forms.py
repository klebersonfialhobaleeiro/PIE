from django import forms
from .models import Relato

class RelatoForm(forms.ModelForm):
    class Meta:
        model = Relato
        fields = ['tipo_problema', 'descricao', 'foto', 'poligono']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'poligono': forms.HiddenInput()
        }
