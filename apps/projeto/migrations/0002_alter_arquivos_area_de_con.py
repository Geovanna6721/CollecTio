# Generated by Django 5.1.1 on 2024-09-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivos',
            name='area_de_con',
            field=models.CharField(choices=[('1', 'Saúde'), ('2', 'Tecnologia'), ('3', 'Linguagens'), ('4', 'Ciências Exatas'), ('5', 'Ciências Humanas')], max_length=3, verbose_name='Área de Conhecimento'),
        ),
    ]
