from django.db import models
from datetime import date

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    peso_inicial = models.FloatField()
    altura = models.FloatField()  # em metros
    nivel_atividade = models.CharField(
    max_length=20,
    choices=[
        ('baixo', 'Sedentário'),
        ('moderado', 'Atividade física moderada'),
        ('alto', 'Atividade física intensa'),
    ],
    default='moderado'
)


    def __str__(self):
        return self.nome

    def imc(self):
        return self.peso_atual() / (self.altura ** 2)

    def peso_ideal(self):
        return 20 * (self.altura ** 2)

    def tmb(self):
        if self.sexo == 'M':
            return 66 + (13.7 * self.peso_atual()) + (5 * self.altura * 100) - (6.8 * self.idade)
        else:
            return 655 + (9.6 * self.peso_atual()) + (1.8 * self.altura * 100) - (4.7 * self.idade)

    def proteina_diaria(self):
        fator = 2.0  # sujeitos ativos
        return self.peso_ideal() * fator

    def peso_atual(self):
        ultimo = self.historicos.order_by('-data').first()
        return ultimo.peso if ultimo else self.peso_inicial

class HistoricoPeso(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='historicos', on_delete=models.CASCADE)
    data = models.DateField(default=date.today)
    peso = models.FloatField()
    gordura = models.FloatField(null=True, blank=True)
    meta_kg = models.FloatField(
        default=0.0,
        help_text="Quilos desejados a perder (-) ou ganhar (+) no mês"
    )
    peso_esperado = models.FloatField(null=True, blank=True, help_text="Peso estimado baseado na meta anterior")

    def meta_calorias_dia(self):
        return (self.meta_kg * 7000) / 30



