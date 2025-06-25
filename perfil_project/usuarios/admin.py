# Register your models here.
from django.contrib import admin
from .models import Perfil, PesoHistorico

class PesoHistoricoInline(admin.TabularInline):
    model = PesoHistorico
    extra = 1  # número de linhas extras vazias exibidas
    readonly_fields = ('data',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'idade', 'peso', 'nivel_atividade', 'imc', 'calorias_para_manter')
    list_filter = ('sexo', 'nivel_atividade')
    search_fields = ('nome',)
    ordering = ('nome',)
    readonly_fields = ('imc', 'peso_ideal', 'tmb', 'calorias_para_manter', 'proteina_diaria')
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'sexo', 'idade', 'altura', 'peso', 'percentual_gordura', 'nivel_atividade')
        }),
        ('Cálculos Automáticos', {
            'fields': ('imc', 'peso_ideal', 'tmb', 'calorias_para_manter', 'proteina_diaria')
        }),
    )
    inlines = [PesoHistoricoInline]