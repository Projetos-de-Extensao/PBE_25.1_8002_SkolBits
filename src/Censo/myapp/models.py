from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class IdentificacaoDomicilio(models.Model):
    nr_casa = models.CharField(max_length=4, verbose_name="Número da casa")
    ENDERECO_CHOICES = [
        ("01", "R. Marina do Sol"),
        ("02", "R. Marina do Frade"),
        ("03", "R. Marina dos Coqueiros"),
        ("04", "R. Marina da Lua"),
        ("05", "R. Marina do Bosque"),
        ('06', "R. Marina Porto Bali"),
        ("07", "R. Marina das Flores"),
        ("08", "R. Marina das Estrelas"),
        ("09", "R. Marina Ponta Leste"),
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
        ("06", 'Hotel ou pensão'),
        ('07', 'Alojamento'),
        ('08', 'OutroS'),
    ]
    tipo_domicilio = models.CharField(max_length=2, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio")


class InformacoesMoradores (models.Model):
    quantidade_moradores31_07_2025 = models.CharField(max_length=2, verbose_name="Quantidade de moradores em 31/07/2025")
    quantidade_criancas_0a9_31_07_2025 = models.CharField(max_length=2, verbose_name="Quantidade de crianças de 0 a 9 anos em 31/07/2025")

    nome_morador = models.CharField(max_length=50, verbose_name="Nome do morador")
    sobrenome_morador = models.CharField(max_length=200, verbose_name="Sobrenome do morador")

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")

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

    relacao_com_responsavel = models.CharField(max_length=3, choices=RELACAO_COM_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável")

    class Meta:
        verbose_name = "Informação de morador"
        verbose_name_plural = "Informações de moradores"

    def __str__(self):
        return f"{self.nome_morador} {self.sobrenome_morador}, Sexo: {self.sexo}, Relação com responsável: {self.relacao_com_responsavel}"

class CaracteristicasDomicilio(models.Model):
    ABASTECIMENTO_CHOICES = [
        (1, 'Rede geral de distribuição'),
        (2, 'Profundo ou artesiano'),
        (3, 'Raso, freático ou cacimba'),
        (4, 'Fonte, nascente ou mina'),
        (5, 'Carro-pipa'),
        (6, 'Água da chuva armazenada'),
        (7, 'Rios, açudes, córregos, lagos e igarapés'),
        (8, 'Outra'),
    ]
    abastecimento = models.IntegerField(choices=ABASTECIMENTO_CHOICES)

    def __str__(self):
        return self.abastecimento

    ACESSO_REDE_CHOICES = [
        (1, 'Sim'),
        (2, 'Nao'),
    ]
    acesso_rede_geral_agua = models.IntegerField(choices=ACESSO_REDE_CHOICES)
    
    def __str__(self):
        return self.acesso_rede_geral_agua

    AGUA_UTILIZADA_CHEGA_CHOICES = [
        (1, 'Encanada até dentro de casa, apartamento ou habitação'),
        (2, 'Encanada, mas apenas no terreno'),
        (3, 'Não chega encanada'),
    ]
    agua_utilizada_chega = models.IntegerField(choices=AGUA_UTILIZADA_CHEGA_CHOICES)

    def __str__(self):
        return self.agua_utilizada_chega

    quantidade_banheiros_exclusivos_com_chuveiro_vaso = models.CharField(max_length=2)

    def __str__(self):
        return self.quantidade_banheiros_exclusivos_com_chuveiro_vaso

    UTILIZA_BANHEIRO_COMUM_CHOICEs = [
        (1, 'Sim'),
        (2, 'Nao'),
    ]
    utiliza_banheiro_comum = models.IntegerField(choices=UTILIZA_BANHEIRO_COMUM_CHOICEs)

    def __str__(self):
        return self.utiliza_banheiro_comum

    UTILIZA_SANITARIOS_BURACOS_DEJECAO_CHOICES = [
        (1, 'Sim'),
        (2, 'Nao'),

    ]
    utiliza_sanitarios_buracos_dejeicao = models.IntegerField(choices=UTILIZA_SANITARIOS_BURACOS_DEJECAO_CHOICES)

    def __str__(self):
        return self.utiliza_sanitarios_buracos_dejeicao

    ONDE_VAI_ESGOTO_BANHEIRO_CHOICES = [
        (1, 'Rede geral ou pluvial'),
        (2, 'Ligada a rede'),
        (3, 'Nao ligada a rede'),
        (4, 'Fossa rudimentar ou buraco'),
        (5, 'Vala'),
        (6, 'Rio, lago, córrego ou mar'),
        (7, 'Outra forma'),
    ]
    onde_vai_esgoto_banheiro = models.IntegerField(choices=ONDE_VAI_ESGOTO_BANHEIRO_CHOICES)

    def __str__(self):
        return self.onde_vai_esgoto_banheiro

    ONDE_VAI_ESGOTO_SANITARIO_BURACO_CHOICES = [
        (1, 'Rede geral ou pluvial'),
        (2, 'Ligada a rede'),
        (3, 'Nao ligada a rede'),
        (4, 'Fossa rudimentar ou buraco'),
        (5, 'Vala'),
        (6, 'Rio, lago, córrego ou mar'),
        (7, 'Outra forma'),
    ]
    onde_vai_esgoto_sanitario_buraco = models.IntegerField(choices=ONDE_VAI_ESGOTO_SANITARIO_BURACO_CHOICES)

    def __str__(self):
        return self.onde_vai_esgoto_sanitario_buraco

    LIXO_CHOICES = [
        (1, 'Coletado no domicilio por serviços de limpeza'),
        (2, 'Depositado em cacamba de serviço de limpeza'),
        (3, 'Queimado na propriedade'),
        (4, 'Enterrado na propriedade'),
        (5, 'Jogado em terreno baldio, encosta ou área pública'),
        (6, 'Outro destino'),
    ]
    lixo = models.IntegerField(choices=LIXO_CHOICES)

    def __str__(self):
        return self.lixo
    

    
    #PAGINA 4
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

    