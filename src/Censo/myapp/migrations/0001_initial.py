# Generated by Django 5.2.1 on 2025-05-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='indentificacao_domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2)),
                ('municipio', models.CharField(max_length=30)),
                ('distrito', models.CharField(max_length=2)),
                ('setor', models.CharField(max_length=4)),
                ('nr_quadra', models.CharField(max_length=3)),
                ('nr_da_face', models.CharField(max_length=3)),
            ],
        ),
    ]
