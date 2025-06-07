from django.db import models

class Domicilio(models.Model):
    nr_casa = models.CharField(max_length=4, verbose_name="Número da casa")
    ENDERECO_CHOICES = [
        ("sol", "R. Marina do Sol"),
        ("frade", "R. Marina do Frade"),
        ("coqueiros", "R. Marina dos Coqueiros"),
        ("lua", "R. Marina da Lua"),
        ("bosque", "R. Marina do Bosque"),
        ("bali", "R. Marina Porto Bali"),
        ("flores", "R. Marina das Flores"),
        ("estrelas", "R. Marina das Estrelas"),
        ("pontaleste", "R. Marina Ponta Leste"),
    ]
    endereco = models.CharField(max_length=20, choices=ENDERECO_CHOICES, verbose_name="Endereço")

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    especie = models.CharField(max_length=3, choices=ESPECIE_CHOICES)

    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('casa_vila_ou_condominio', 'Casa de vila ou em condomínio'),
        ('casa_comodos_ou_cortiço', 'Habitação em casa de cômodos ou cortiço'),
        ('estrututura_degradada_ou_inacabada', 'Estrutura não residencial permanente degradada ou inacabada'),
        ('asilo', 'Asilo ou outra instrituição de longa permanência'),
        ("hotel_ou_pensao", 'Hotel ou pensão'),
        ('alojamento', 'Alojamento'),
        ('outros', 'Outros'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio")

    CONDIÇÃO_POSSE_CHOICES = [
        ('pagando', 'Ainda pagando'),
        ('alugada', 'Alugada'),
        ('por_empregador', 'Por empregador'),
        ('por_familiar', 'Por familiar'),
        ('outra_forma', 'Outra forma'),
        ('outra_condicao', 'Outra condição'),
        ('ja_pago', 'Já pago, herdado ou ganho'),
    ]
    condicao_posse = models.CharField(max_length=50, choices=CONDIÇÃO_POSSE_CHOICES, verbose_name="Condição de posse do domicílio")

    ABASTECIMENTO_CHOICES = [
        ('rede_geral', 'Rede geral de distribuição'),
        ('poco_artesiano', 'Poço artesiano'),
        ('cacimba', 'Cacimba'),
        ('rio_lago_corregos_ou_represas', 'Rio, lago, córregos ou represas'),
        ('fonte_nascente_ou_mina', 'fonte, nascente ou mina'),
        ('carro-pipa', 'carro-pipa'),
        ('agua_de_chuva', 'água de chuva'),
        ('outro', 'Outro'),
    ]
    abastecimento = models.CharField(max_length=50, choices=ABASTECIMENTO_CHOICES, verbose_name="Abastecimento de água")

    ESGOTO_CHOICES = [
        ('Rede geral de esgoto', 'Rede geral de esgoto'),
        ('Fossa séptica', 'Fossa séptica'),
        ('Fossa rudimentar', 'Fossa rudimentar'),
        ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
        ('Vala', 'Vala'),
        ('Outro', 'Outro'),
    ]
    esgoto = models.CharField(max_length=50, choices=ESGOTO_CHOICES, verbose_name="Esgoto")

    DISTRIBUICAO_AGUA_CHOICES = [
        ('Encanada até dentro da moradia', 'Encanada até dentro da moradia'),
        ('Encanada, mas apenas terreno ou quintal', 'Encanada, mas apenas terreno ou quintal'),
        ('Não encanada', 'Não encanada'),
    ]
    distribuicao_agua = models.CharField(max_length=50, choices=DISTRIBUICAO_AGUA_CHOICES, verbose_name="Distribuição de água")

    LIXO_CHOICES = [
        ('coletado_prefeitura', 'Coletado pela prefeitura'),
        ('coletado_empresa', 'Coletado por empresa particular'),
        ('queimado', 'Queimado'),
        ('enterrado', 'Enterrado'),
        ('jogado_terreno_baldio', 'Jogado em terreno baldio'),
        ('jogado_rio_lago_corrego_represa', 'Jogado em rio, lago, córrego ou represa'),
        ('outro', 'Outro'),
    ]
    lixo = models.CharField(max_length=50, choices=LIXO_CHOICES, verbose_name="Destinação do lixo")