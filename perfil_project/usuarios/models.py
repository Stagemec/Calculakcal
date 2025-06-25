from django.db import models

NIVEL_ATIVIDADE = [
    ('1.2', 'Sedentário'),
    ('1.375', 'Levemente ativo'),
    ('1.55', 'Moderadamente ativo'),
    ('1.725', 'Muito ativo'),
    ('1.9', 'Extremamente ativo'),
]


def proteina_diaria(self):
    # Mapeia o nível de atividade para o fator de proteína
    mapa_fator = {
        '1.2': 0.8,
        '1.375': 1.2,
        '1.55': 1.4,
        '1.725': 1.6,
        '1.9': 2.0,
    }
    fator = mapa_fator.get(self.nivel_atividade, 1.2)
    return round(self.peso_ideal() * fator, 2)

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    idade = models.PositiveIntegerField()
    altura = models.FloatField(help_text="Em metros")
    peso = models.FloatField(help_text="Em kg")
    percentual_gordura = models.FloatField(null=True, blank=True)
    nivel_atividade = models.CharField(max_length=5, choices=NIVEL_ATIVIDADE, default='1.2')

    def __str__(self):
        return self.nome

    def imc(self):
        return round(self.peso / (self.altura ** 2), 2)

    def imc_classificacao(self):
        valor = self.imc()
        if valor < 18.5:
            return "Baixo peso"
        elif valor < 25:
            return "Peso normal"
        elif valor < 30:
            return "Sobrepeso"
        elif valor < 35:
            return "Obesidade grau I"
        elif valor < 40:
            return "Obesidade grau II (severa)"
        return "Obesidade grau III (mórbida)"

    def imc_cor(self):
        valor = self.imc()
        if valor < 18.5 or valor >= 30:
            return "red"
        elif valor < 25:
            return "green"
        return "orange"

    def peso_ideal(self):
        return round(25 * (self.altura ** 2), 2)

    def tmb(self):
        altura_cm = self.altura * 100
        if self.sexo == 'M':
            return round(88.362 + (13.397 * self.peso) + (4.799 * altura_cm) - (5.677 * self.idade), 2)
        return round(447.593 + (9.247 * self.peso) + (3.098 * altura_cm) - (4.330 * self.idade), 2)

    def calorias_para_manter(self):
        return round(self.tmb() * float(self.nivel_atividade), 2)

    def proteina_diaria(self):
        return round(self.peso_ideal() * float(self.fator_proteina), 2)

    def estimativa_meta(self, kg=3, ganhar=True):
        ajuste = (7000 * kg) / 30
        manter = self.calorias_para_manter()
        return round(manter + ajuste, 2) if ganhar else round(manter - ajuste, 2)

    def estimativa_mensal(self, kg=3, ganhar=True):
        return round(self.estimativa_meta(kg=kg, ganhar=ganhar) * 30, 2)

class PesoHistorico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='historicos')
    peso = models.FloatField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.peso} kg em {self.data}"
