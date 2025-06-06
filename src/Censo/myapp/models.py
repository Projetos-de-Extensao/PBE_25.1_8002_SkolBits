from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class IdentificacaoDomicilio(models.Model):
    uf = models.CharField(max_length=2, verbose_name="UF")
    municipio = models.CharField(max_length=30, verbose_name="Município")
    distrito = models.CharField(max_length=2, verbose_name="Distrito")
    setor = models.CharField(max_length=4, verbose_name="Setor")
    nr_quadra = models.CharField(max_length=3, verbose_name="Número da quadra")
    nr_da_face = models.CharField(max_length=3, verbose_name="Número da face")

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    especie = models.CharField(max_length=3, choices=ESPECIE_CHOICES)

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
    
    tipo_domicilio = models.CharField(max_length=3, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio")

    class Meta:
        verbose_name = "Identificação de domicílio"
        verbose_name_plural = "Identificações de domicílio"

    def __str__(self):
        return f"Domicílio em {self.municipio}, UF: {self.uf}"

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

    