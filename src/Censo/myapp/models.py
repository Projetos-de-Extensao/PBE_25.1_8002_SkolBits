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

    ABASTECIMENTO_AGUA_CHOICES = [
        ('rede_geral', 'Rede geral de distribuição'),
        ('poco_artesiano', 'Poço artesiano'),
        ('cacimba', 'Cacimba'),
        ('rio_lago_corregos_ou_represas', 'Rio, lago, córregos ou represas'),
        ('fonte_nascente_ou_mina', 'fonte, nascente ou mina'),
        ('carro-pipa', 'carro-pipa'),
        ('agua_de_chuva', 'água de chuva'),
        ('outro', 'Outro'),
    ]
    abastecimento_agua = models.CharField(max_length=50, choices=ABASTECIMENTO_AGUA_CHOICES, verbose_name="Abastecimento de água")

    DISTRIBUICAO_AGUA_CHOICES = [
        ('Encanada até dentro da moradia', 'Encanada até dentro da moradia'),
        ('Encanada, mas apenas terreno ou quintal', 'Encanada, mas apenas terreno ou quintal'),
        ('Não encanada', 'Não encanada'),
    ]
    distribuicao_agua = models.CharField(max_length=50, choices=DISTRIBUICAO_AGUA_CHOICES, verbose_name="Distribuição de água")
    
    ABASTECIMENTO_ENERGIA_CHOICES = [
        ('rede_geral', 'Rede geral de distribuição'),
        ('gerador', 'Gerador'),
        ('energia_solar', 'Energia solar'),
        ('energia_eolica', 'Energia eólica'),
        ('energia_hidraulica', 'Energia hidráulica'),
        ('outra_fonte', 'Outra fonte'),
    ]
    abastecimento_energia = models.CharField(max_length=50, choices=ABASTECIMENTO_ENERGIA_CHOICES, verbose_name="Abastecimento de energia")

    CHEGA_ENERGIA_INTERNET_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    chega_energia_internet = models.CharField(max_length=3, choices=CHEGA_ENERGIA_INTERNET_CHOICES, verbose_name="Chega energia e internet?")
    
    ESGOTO_CHOICES = [
        ('Rede geral de esgoto', 'Rede geral de esgoto'),
        ('Fossa séptica', 'Fossa séptica'),
        ('Fossa rudimentar', 'Fossa rudimentar'),
        ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
        ('Vala', 'Vala'),
        ('Outro', 'Outro'),
    ]
    esgoto = models.CharField(max_length=50, choices=ESGOTO_CHOICES, verbose_name="Esgoto")

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

    quantidade_comodos = models.IntegerField(verbose_name="Quantidade de cômodos", null=True, blank=True)
    quantidade_dormitorios = models.IntegerField(verbose_name="Quantidade de dormitórios", null=True, blank=True)
    banheiros = models.IntegerField(verbose_name="Banheiros", null=True, blank=True)

class Morador (models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do morador")
    sobrenome = models.CharField(max_length=200, verbose_name="Sobrenome do morador")

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")

    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    RELACAO_COM_RESPONSAVEL_CHOICES = [
        ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicilio'),
        ('conjuge_ou_companheiro(a)_de_sexo_diferente', 'Cônjuge ou companheiro(a) de sexo diferente'),
        ('conjuge_ou_companheiro(a)_do_mesmo_sexo', 'Cônjuge ou companheiro(a) do mesmo sexo'),
        ('filho(a)_do_responsavel_e_do_conjuge', 'Filho(a) do responsável e do cônjuge'),
        ('filho(a)_somente_do_responsavel', 'Filho(a) somente do responsável'),
        ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicílio'),
        ('genro_ou_nora', 'Genro ou nora'),
        ('pai_mae_padrasto_ou_madrasta', 'Pai, mãe, padrasto ou madrasta'),
        ('sogro(a)', 'Sogro(a)'),
        ('neto(a)', 'Neto(a)'),
        ('enteado(a)', 'Enteado(a)'),
        ('irmão_ou_irma', 'Irmão ou irmã'),
        ('avô_ou_avo', 'Avô ou avó'),
        ('outroparente', 'Outro parente'),
        ('agregado(a)', 'Agregado(a)'),
        ('bisneto(a)', 'Bisneto(a)'),
        ('pensionista', 'Pensionista'),
        ('empregado(a)_domestico(a)', 'Empregado(a) doméstico(a)'),
        ('parente_do(a)_empregado(a)_domestico(a)', 'Parente do(a) empregado(a) doméstico(a)'),
        ('individual_em_domicilio_coletivo', 'Individual em domicílio coletivo'),
    ]
    relacao_com_responsavel = models.CharField(max_length=100, choices=RELACAO_COM_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável pelo domicílio")

    REGISTRO_DE_NASCIMENTO_CHOICES = [
        ('do_cartorio', 'Do cartório'),
        ('registro_administrativo_de_nascimento_indígena', 'Registro administrativo de nascimento indígena'),
        ('nao_tem', 'Não tem'),
        ('nao_sabe', 'Não sabe'),
    ]
    registro_de_nascimento = models.CharField(max_length=100, choices=REGISTRO_DE_NASCIMENTO_CHOICES, verbose_name="Tem registro de nascimento?")

    NUPICIALIDADE_CHOICES = [
        ('possui_conjuge_ou_companheiro(a)', 'Possui conjuge ou companheiro(a)'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    nupicialidade = models.CharField(max_length=50, choices=NUPICIALIDADE_CHOICES, verbose_name="Nupicialidade")

    VIVEM_COMPANHIA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    vivem_companhia = models.CharField(max_length=3, choices=VIVEM_COMPANHIA_CHOICES, verbose_name="Vivem com companhia de conjuge ou companheiro(a)?")

    nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do cônjuge", blank=True, null=True)

    TIPO_UNIAO_CHOICES = [
        ('casamento_civil_e_religioso', 'Casamento civil e religioso'),
        ('so_casamento_civil', 'So casamento civil'),
        ('so_casamento_religioso', 'So casamento religioso'),
        ('uniao_consensual', 'União consensual'),
    ]
    tipo_uniao = models.CharField(max_length=50, choices=TIPO_UNIAO_CHOICES, verbose_name="Tipo de união")

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
    numero_de_trabalhos = models.CharField(max_length=20, choices=NUMERO_DE_TRABALHOS_CHOICES, verbose_name="Quantos trabalhos tinha nos últimos meses?")
    
    ocupacao_funcao = models.TextField(max_length=400, verbose_name="Qual era a ocupação, cargo ou função que tinha nesse trabalho?")

    atividade_negocio = models.TextField(max_length=400, verbose_name="Qual era a principal atividade do negócio ou empresa em que tinha esse trabalho?")
    
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
