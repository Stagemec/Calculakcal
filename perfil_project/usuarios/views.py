# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil, PesoHistorico
from .forms import PerfilForm
from django.shortcuts import redirect

def perfil_detalhe(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    return render(request, 'usuarios/perfil_detalhe.html', {'perfil': perfil})


def criar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save()  # 👈 salva e armazena a instância
            return redirect('perfil_detalhe', pk=perfil.pk)  # 👈 redireciona corretamente
    else:
        form = PerfilForm()
    return render(request, 'usuarios/perfil_form.html', {'form': form})
    

from .forms import MetaPesoForm

def calcular_meta(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    resultado = None

    if request.method == 'POST':
        form = MetaPesoForm(request.POST)
        if form.is_valid():
            objetivo = form.cleaned_data['objetivo']
            kg = form.cleaned_data['quantidade_kg']
            ganhar = objetivo == 'ganhar'
            calorias_dia = perfil.estimativa_meta(kg=kg, ganhar=ganhar)
            calorias_mes = perfil.estimativa_mensal(kg=kg, ganhar=ganhar)
            resultado = {
                'objetivo': objetivo,
                'kg': kg,
                'dia': calorias_dia,
                'mes': calorias_mes
            }
    else:
        form = MetaPesoForm()

    return render(request, 'usuarios/calcular_meta.html', {'perfil': perfil, 'form': form, 'resultado': resultado})


def grafico_peso(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    historico = perfil.historicos.order_by('data')

    datas = [h.data.strftime('%d/%m') for h in historico]
    pesos = [h.peso for h in historico]

    return render(request, 'usuarios/grafico_peso.html', {
        'perfil': perfil,
        'datas': datas,
        'pesos': pesos,
        'historico': historico,  # 👈 passamos os dados pra tabela
    })


def atualizar_peso(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        novo_peso = float(request.POST.get('peso'))
        perfil.peso = novo_peso
        perfil.save()
        PesoHistorico.objects.create(perfil=perfil, peso=novo_peso)  # 🎯 Registro automático!
        return redirect('perfil_detalhe')
    return render(request, 'usuarios/atualizar_peso.html', {'perfil': perfil})

def excluir_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == 'POST':
        perfil.delete()
        return redirect('criar_perfil')
    

def home(request):
    perfil = Perfil.objects.first()
    if perfil:
        return redirect('perfil_detalhe', pk=perfil.pk)  # ✅ necessário passar o ID
    return redirect('criar_perfil')