from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class IdentificacaoDomicilio(models.Model):
    nr_casa = models.CharField(max_length=4, verbose_name="Número da casa")
    ENDERECO_CHOICES = [
        ('01', "R. Marina do Sol"),
        ('02', "R. Marina do Frade"),
        ('03', "R. Marina dos Coqueiros"),
        ('04', "R. Marina da Lua"),
        ('05', "R. Marina do Bosque"),
        ('06', "R. Marina Porto Bali"),
        ('07', "R. Marina das Flores"),
        ('08', "R. Marina das Estrelas"),
        ('09', "R. Marina Ponta Leste"),
    ]
    endereco = models.CharField(max_length=2, choices=ENDERECO_CHOICES, verbose_name="Endereço")

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    especie = models.CharField(max_length=3, choices=ESPECIE_CHOICES)

    TIPO_CHOICES = [
        ('01', 'Casa'),
        ('02', 'Casa de vila ou em condomínio'),
        ('03', 'Habitação em casa de cômodos ou cortiço'),
        ('04', 'Estrutura não residencial permanente degradada ou inacabada'),
        ('05', 'Asilo ou outra instrituição de longa permanência'),
        ('06', 'Hotel ou pensão'),
        ('07', 'Alojamento'),
        ('08', 'OutroS'),
    ]
    tipo_domicilio = models.CharField(max_length=2, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio")


class InformacoesMoradores (models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do morador")
    sobrenome = models.CharField(max_length=200, verbose_name="Sobrenome do morador")

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")

    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    RELACAO_COM_RESPONSAVEL_CHOICES = [
        ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicilio')
        ('conjuge_ou_companheiro(a)_de_sexo_diferente', 'Cônjuge ou companheiro(a) de sexo diferente')
        ('conjuge_ou_companheiro(a)_do_mesmo_sexo', 'Cônjuge ou companheiro(a) do mesmo sexo')
        ('filho(a)_do_responsavel_e_do_conjuge', 'Filho(a) do responsável e do cônjuge')
        ('filho(a)_somente_do_responsavel', 'Filho(a) somente do responsável')
        ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicílio')
        ('genro_ou_nora', 'Genro ou nora')
        ('pai_mae_padrasto_ou_madrasta', 'Pai, mãe, padrasto ou madrasta')
        ('sogro(a)', 'Sogro(a)')
        ('neto(a)', 'Neto(a)')
        ('enteado(a)', 'Enteado(a)')
        ('irmão_ou_irma', 'Irmão ou irmã')
        ('avô_ou_avo', 'Avô ou avó')
        ('outroparente', 'Outro parente')
        ('agregado(a)', 'Agregado(a)')
        ('bisneto(a)', 'Bisneto(a)')
        ('pensionista', 'Pensionista')
        ('empregado(a)_domestico(a)', 'Empregado(a) doméstico(a)')
        ('parente_do(a)_empregado(a)_domestico(a)', 'Parente do(a) empregado(a) doméstico(a)')
        ('individual_em_domicilio_coletivo', 'Individual em domicílio coletivo')
    ]
    relacao_com_responsavel = models.CharField(max_length=3, choices=RELACAO_COM_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável pelo domicílio")

    REGISTRO_DE_NASCIMENTO_CHOICES = [
        ('do_cartorio', 'Do cartório'),
        ('registro_administrativo_de_nascimento_indígena', 'Registro administrativo de nascimento indígena'),
        ('nao_tem', 'Não tem'),
        ('nao_sabe', 'Não sabe'),
    ]
    registro_de_nascimento = models.CharField(max_length=2, choices=REGISTRO_DE_NASCIMENTO_CHOICES, verbose_name="Tem registro de nascimento?")

    NUPICIALIDADE_CHOICES = [
        ('possui_conjuge_ou_companheiro(a)', 'Possui conjuge ou companheiro(a)'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    nupicialidade = models.CharField(max_length=2, choices=NUPICIALIDADE_CHOICES, verbose_name="Nupicialidade")

    VIVEM_COMPANHIA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    vivem_companhia = models.CharField(max_length=2, choices=VIVEM_COMPANHIA_CHOICES, verbose_name="Vivem com companhia de conjuge ou companheiro(a)?")

    nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do cônjuge", blank=True, null=True)

    TIPO_UNIAO_CHOICES = [
        ('casamento_civil_e_religioso', 'Casamento civil e religioso'),
        ('so_casamento_civil', 'So casamento civil'),
        ('so_casamento_religioso', 'So casamento religioso'),
        ('uniao_consensual', 'União consensual'),
    ]
    tipo_uniao = models.CharField(max_length=2, choices=TIPO_UNIAO_CHOICES, verbose_name="Tipo de união")

    TRABALHOU_OU_ESTAGIOU_CHOICES = [
    ("SIM", "Sim"),
    ("NAO", "Não"),
    ]
    trabalhou_ou_estagiou = models.CharField(max_length=3, choices=TRABALHOU_OU_ESTAGIOU_CHOICES, verbose_name="Trabalhou ou estagiou em alguma atividade remunerada em dinheiro?")

    NUMERO_DE_TRABALHOS_CHOICES = [
    ("um", "1"),
    ("dois", "2"),
    ("tres_ou_mais", "3 ou mais"),
    ]
    numero_de_trabalhos = models.CharField(max_length=3, choices=NUMERO_DE_TRABALHOS_CHOICES, verbose_name="Quantos trabalhos tinha nos últimos meses?")
    
    ocupacao_funcao = models.StringField(max_length=400, verbose_name="Qual era a ocupação, cargo ou função que tinha nesse trabalho?")

    atividade_negocio = models.StringField(max_length=400, verbose_name="Qual era a principal atividade do negócio ou empresa em que tinha esse trabalho?")
    
    CARTEIRA_ASSINADA_CHOICES = [
    ("sim", "Sim"),
    ("nao", "Não"),
    ]
    carteira_assinada = models.CharField(max_length=3, choices=CARTEIRA_ASSINADA_CHOICES, verbose_name="Nesse trabalho tinha carteira de trabalho assinada?")

    EMPRESA_COM_CNPJ_CHOICES = [
    ("sim", "Sim"),
    ("nao", "Não"),
    ]
    empresa_com_cnpj = models.CharField(max_length=3, choices=EMPRESA_COM_CNPJ_CHOICES, verbose_name="Esse negócio ou empresa era registrado no cadastro nacional de pessoa jurídica - cnpj?")

    FAIXA_DE_RENDIMENTO_CHOICES = [
    ("faixa_1_ate_500", "1 - 1,00 a 500,00"),
    ("faixa_2_501_a_1000", "2 - 501,00 a 1.000,00"),
    ("faixa_3_1001_a_2000", "3 - 1.001,00 a 2.000,00"),
    ("faixa_4_2001_a_3000", "4 - 2.001,00 a 3.000,00"),
    ("faixa_5_3001_a_5000", "5 - 3.001,00 a 5.000,00"),
    ("faixa_6_5001_a_10000", "6 - 5.001,00 a 10.000,00"),
    ("faixa_7_10001_a_20000", "7 - 10.001,00 a 20.000,00"),
    ("faixa_8_20001_a_100000", "8 - 20.001,00 a 100.000,00"),
    ("faixa_9_mais_de_100000", "9 - 100.001 ou mais"),
    ]
    faixa_de_rendimento = models.CharField(max_length=25, choices=FAIXA_DE_RENDIMENTO_CHOICES, verbose_name="Faixa de rendimento")

    FALECEU_ALGUEM_CHOICES = [
    ("sim", "Sim"),
    ("nao", "Não"),
    ]
    faleceu_algum = models.CharField(max_length=3, choices=FALECEU_ALGUEM_CHOICES, verbose_name="Faleceu alguma pessoa que morava com você(s)? (inclusive recém-nascidos e idosos)")

class CaracteristicasAdicionaisMoradores(models.Model):
    cor_raca_CHOICES = [
        (1, 'Branca'),
        (2, 'Preta'),
        (3, 'Parda'),
        (4, 'Amarela'),
        (5, 'Indígena'),
    ]
    cor_raca = models.IntegerField(choices=cor_raca_CHOICES, verbose_name="Cor/Raça")

    def __str__(self):
        return self.cor_raca
    
    considera_se_indigena_CHOICES = [
        (1, 'Sim'),
        (2, 'Não'),
    ]
    considera_se_indigena = models.IntegerField(choices=considera_se_indigena_CHOICES, verbose_name="Considera-se indígena", default=2)
    def __str__(self):
        return self.considera_se_indigena
    
    etinia_1 = models.CharField(max_length=2, verbose_name="Etinia 1")
    etinia_2 = models.CharField(max_length=2, verbose_name="Etinia 2", blank=True, null=True)

    