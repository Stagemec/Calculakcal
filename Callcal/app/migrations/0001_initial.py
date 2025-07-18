# Generated by Django 5.2.3 on 2025-06-27 19:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('peso_inicial', models.FloatField()),
                ('altura', models.FloatField()),
                ('nivel_atividade', models.CharField(choices=[('baixo', 'Baixo'), ('moderado', 'Moderado'), ('alto', 'Alto')], default='moderado', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoPeso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.date.today)),
                ('peso', models.FloatField()),
                ('gordura', models.FloatField()),
                ('meta_kcal', models.IntegerField(blank=True, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='app.perfil')),
            ],
        ),
    ]
