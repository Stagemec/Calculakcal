# Generated by Django 5.2.3 on 2025-06-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicopeso',
            name='meta_kcal',
        ),
        migrations.AddField(
            model_name='historicopeso',
            name='meta_kg',
            field=models.FloatField(default=0.0, help_text='Quilos desejados a perder (-) ou ganhar (+) no mês'),
        ),
    ]
