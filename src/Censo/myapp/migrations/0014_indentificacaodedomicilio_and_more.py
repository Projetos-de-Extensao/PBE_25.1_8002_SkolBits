# Generated by Django 5.2.1 on 2025-06-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_indentificaçãodedomicilio_remove_domicilio_endereco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndentificacaoDeDomicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(choices=[('sol', 'R. Marina do Sol'), ('frade', 'R. Marina do Frade'), ('coqueiros', 'R. Marina dos Coqueiros'), ('lua', 'R. Marina da Lua'), ('bosque', 'R. Marina do Bosque'), ('bali', 'R. Marina Porto Bali'), ('flores', 'R. Marina das Flores'), ('estrelas', 'R. Marina das Estrelas'), ('pontaleste', 'R. Marina Ponta Leste')], max_length=20, verbose_name='Endereço')),
                ('nr_casa', models.CharField(max_length=4, verbose_name='Número da casa')),
                ('especie', models.CharField(blank=True, choices=[('DPP', 'Domicílio particular permanente ocupado'), ('DPI', 'Domicílio particular improvisado ocupado'), ('DCM', 'Domicílio coletivo com morador')], max_length=3, null=True, verbose_name='Espécie do domicílio')),
            ],
        ),
        migrations.DeleteModel(
            name='IndentificaçãoDeDomicilio',
        ),
    ]
