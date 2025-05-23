from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class IdentificacaoDomicilio(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=30)
    distrito = models.CharField(max_length=2)
    setor = models.CharField(max_length=4)
    nr_quadra = models.CharField(max_length=3)
    nr_da_face = models.CharField(max_length=3)

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    especie = models.CharField(max_length=3, choices=ESPECIE_CHOICES, default='DPP')

    TIPO_CHOICES = [
        ('001', 'Casa'),
        ('002', 'Casa de vila ou em condomínio'),
        ('003', 'Apartamento'),
        ('004', 'Habitação em casa de cômodos ou cortiço'),
        ('005', 'Habitação indígena sem paredes ou maloca'),
        ('006', 'Estrutura residencial permanente degradada ou inacabada'),
        ('007', 'Tenda ou barraca de lona.plástico ou tecido'),
        ('008', 'Dentro do estabelecimento em funcionamento'),
        ('009', 'Outros (Abrigos naturais e outras estruturas improvisadas)'),
        ('010', 'Estrutura improvisada em logradouro público, exceto tenda ou barraca'),
        ('011', 'Estrutura não residencial permanente degradada ou inacabada'),
        ('012', 'Veículos (carros, caminhões, trailers, barcos etc)'),
        ('013', 'Asilo ou outra instrituição de longa permanência'),
        ("014", 'Hotel ou pensão'),
        ('015', 'Alojamento'),
        ('016', 'Penitenciária, centro de detenção e similar'),
        ('017', 'Outro'),
        ('018', 'Abrigo, albergue ou casa de passagem para população em situação de rua'),
        ('019', 'Abrigo, casas de passagem ou república assistencial para outros grupos vulneraveis'),
        ('020', 'Clinica psiquiátrica,  comunidade terapêutica e similar'),
        ('021', 'Orfanato e similar'),
        ('022', 'Unidade de internação para de menores'),
        ('023', 'Quartel ou outra ornganização militar'),
    ]
    
    tipo_domicilio = models.CharField(max_length=3, choices=TIPO_CHOICES, default='001')

    def __str__(self):
        return f"Domicílio em {self.municipio}, UF: {self.uf}"
