from django import forms
from .models import Perfil
from .models import HistoricoPeso

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'idade', 'sexo', 'peso_inicial', 'altura', 'nivel_atividade']

class HistoricoPesoForm(forms.ModelForm):
    class Meta:
        model = HistoricoPeso
        fields = ['peso', 'gordura', 'meta_kg']
