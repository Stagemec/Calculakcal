from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Perfil
import json
from .forms import PerfilCadastroForm
from .forms import PerfilAtualizacaoForm, PerfilAtividadeForm, HistoricoPesoForm
from datetime import timedelta


def boas_vindas(request):
    return render(request, 'app/boas_vindas.html')

def lista_perfis(request):
    perfis = Perfil.objects.all()
    return render(request, 'app/lista_perfis.html', {'perfis': perfis})

def cadastro_perfil(request):
    if request.method == 'POST':
        form = PerfilCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perfis')
    else:
        form = PerfilCadastroForm()
    return render(request, 'app/cadastro_perfil.html', {'form': form})


def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def calcular_proteina_por_atividade(peso, nivel):
    if nivel == 'baixo':
        return peso * 0.8
    elif nivel == 'moderado':
        return peso * 1.4  # média entre 1.2 e 1.6
    elif nivel == 'alto':
        return peso * 2.0  # média entre 1.6 e 2.2
    return peso * 1.2  # fallback seguro


def detalhes_perfil(request, perfil_id):
    from datetime import date

    perfil = get_object_or_404(Perfil, id=perfil_id)
    peso_atual = perfil.peso_atual()
    imc = perfil.imc()
    imc_status = interpretar_imc(imc)
    peso_ideal = perfil.peso_ideal()
    tmb = perfil.tmb()

    historico = perfil.historicos.order_by('data')
    historico_dias = []
    pesos = []
    gorduras = []
    pesos_esperados = []

    for h in historico:
        historico_dias.append(h.data.strftime('%d/%m'))
        pesos.append(h.peso)
        gorduras.append(h.gordura if h.gordura is not None else None)
        pesos_esperados.append(h.peso_esperado if h.peso_esperado is not None else None)

    ultimo = historico.last()
    meta_kg = ultimo.meta_kg if ultimo else 0
    meta_kcal_dia = ultimo.meta_calorias_dia() if ultimo else 0

    fatores_tmb = {'baixo': 1.2, 'moderado': 1.55, 'alto': 1.9}
    fator = fatores_tmb.get(perfil.nivel_atividade, 1.55)
    tmb_ajustado = tmb * fator
    meta_total_kcal = tmb_ajustado + meta_kcal_dia
    proteina_ideal = calcular_proteina_por_atividade(perfil.peso_ideal(), perfil.nivel_atividade)

    contexto = {
        'perfil': perfil,
        'peso_atual': peso_atual,
        'imc': imc,
        'imc_status': imc_status,
        'peso_ideal': peso_ideal,
        'tmb': tmb,
        'tmb_ajustado': tmb_ajustado,
        'meta_kg': meta_kg,
        'meta_kcal_dia': meta_kcal_dia,
        'meta_total_kcal_dia': meta_total_kcal,
        'proteina': proteina_ideal,
        'grafico_labels': json.dumps(historico_dias),
        'grafico_pesos': json.dumps(pesos),
        'grafico_gordura': json.dumps(gorduras),
        'grafico_esperado': json.dumps(pesos_esperados),
    }

    return render(request, 'app/detalhes_perfil.html', contexto)

    
def registrar_atualizacao(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)

    if request.method == 'POST':
        form_historico = HistoricoPesoForm(request.POST)
        form_atividade = PerfilAtividadeForm(request.POST, instance=perfil)

        if form_historico.is_valid() and form_atividade.is_valid():
            historico = form_historico.save(commit=False)
            historico.perfil = perfil

            anterior = perfil.historicos.order_by('-data').first()
            if anterior:
                historico.peso_esperado = anterior.peso + historico.meta_kg
            else:
                historico.peso_esperado = historico.peso

            historico.save()
            form_atividade.save()

            return redirect('detalhes_perfil', perfil_id=perfil.id)
    else:
        form_historico = HistoricoPesoForm()
        form_atividade = PerfilAtividadeForm(instance=perfil)

    return render(request, 'app/registrar_atualizacao.html', {
        'perfil': perfil,
        'form_historico': form_historico,
        'form_atividade': form_atividade,
    })

def editar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        form = PerfilAtualizacaoForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('detalhes_perfil', perfil.id)
    else:
        form = PerfilAtualizacaoForm(instance=perfil)
    return render(request, 'app/editar_perfil.html', {'form': form, 'perfil': perfil})

@require_POST
def excluir_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    perfil.delete()
    return redirect('lista_perfis')
