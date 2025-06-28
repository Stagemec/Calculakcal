from django import forms
from .models import Perfil
from .models import HistoricoPeso

class PerfilCadastroForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'idade', 'sexo', 'peso_inicial', 'altura', 'nivel_atividade']

class PerfilAtualizacaoForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['idade', 'sexo', 'altura']


class HistoricoPesoForm(forms.ModelForm):
    class Meta:
        model = HistoricoPeso
        fields = ['peso', 'gordura', 'meta_kg']

class PerfilAtividadeForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nivel_atividade']
