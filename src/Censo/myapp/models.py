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

class InformacoesMoradores (models.Model):
    quantidade_moradores31_07_2025 = models.CharField(max_length=2)
    quantidade_criancas_0a9_31_07_2025 = models.CharField(max_length=2)

    nome_morador = models.CharField(max_length=50)
    sobrenome_morador = models.CharField(max_length=200)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')

    RELACAO_COM_RESPONSAVEL_CHOICES = [
        ('001', 'Pessoa responsável pelo domicílio'),
        ('002', 'Conjuge ou companheiro(a) de sexo diferente'),
        ('003', 'conjuge ou companheiro(a) de mesmo sexo'),
        ('004', 'Filho(a) do responsável e conjugue'),
        ('005', 'Filho(a) somente do responsável'),
        ('006', 'Enteado(a)'),
        ('007', 'Genro ou nora'),
        ('008', 'Pai, Mãe, Padrasto ou Madrasta'),
        ('009', 'Sogro(a)'),
        ('010', 'Neto(a)'),
        ('011', 'Bisneto(a)'),
        ('012', 'Irmão ou irmã'),
        ('013', 'Avô ou avó'),
        ('014', 'Outro parente'),
        ('015', 'Agregado(a)'),
        ('016', 'Convivente'),
        ('017', 'Pensionista'),
        ('018', 'Empregado(a) doméstico(a)'),
        ('019', 'Parente do(a) empregado(a) doméstico(a)'),
        ('020', 'Indiviual em domicílio coletivo'),
    ]

    relacao_com_responsavel = models.CharField(max_length=3, choices=RELACAO_COM_RESPONSAVEL_CHOICES, default='001')