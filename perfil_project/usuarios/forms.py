from django import forms
from .models import Perfil

OBJETIVOS = [
    ('ganhar', 'Ganhar Peso'),
    ('perder', 'Perder Peso')
]

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        widgets = {
            'nivel_atividade': forms.Select(),
            'fator_proteina': forms.Select()
        }

class MetaPesoForm(forms.Form):
    objetivo = forms.ChoiceField(choices=OBJETIVOS, label="Objetivo")
    quantidade_kg = forms.FloatField(min_value=0.1, label="Quantos kg?")