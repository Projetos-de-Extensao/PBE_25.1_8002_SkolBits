# Generated by Django 5.2.1 on 2025-06-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_delete_domicilio_delete_morador'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_nascimento', models.CharField(blank=True, choices=[('do_cartorio', 'Do cartório'), ('nao_tem', 'Não tem'), ('nao_sabe', 'Não sabe')], max_length=12, null=True, verbose_name='Registro de nascimento')),
            ],
        ),
    ]
