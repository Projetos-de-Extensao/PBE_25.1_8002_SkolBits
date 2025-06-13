from django.db import models
from django.core.validators import MaxValueValidator

class Domicilio(models.Model):
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

    nr_casa = models.CharField(max_length=4, verbose_name="Número da casa")

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    especie = models.CharField(max_length=3, choices=ESPECIE_CHOICES, verbose_name="Espécie do domicílio", blank=True, null=True)

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
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio", blank=True, null=True)

    CONDICAO_POSSE_CHOICES = [
        ('proprio_pago', 'Próprio já pago'),
        ('proprio_pagando', 'Próprio ainda pagando'),
        ('alugado', 'Alugado'),
        ('cedido', 'Cedido'),
        ('ocupacao', 'Ocupação'),
        ('outros', 'Outros'),
    ]
    condicao_posse = models.CharField(max_length=20, choices=CONDICAO_POSSE_CHOICES, verbose_name="Condição de posse", blank=True, null=True)

    ABASTECIMENTO_AGUA_CHOICES = [
        ('rede_geral', 'Rede geral'),
        ('poco_nascente', 'Poço ou nascente'),
        ('caminhao_pipa', 'Caminhão pipa'),
        ('outros', 'Outros'),
    ]
    abastecimento_agua = models.CharField(max_length=20, choices=ABASTECIMENTO_AGUA_CHOICES, verbose_name="Abastecimento de água", blank=True, null=True)

    DISTRIBUICAO_AGUA_CHOICES = [
        ('encanada_moradia', 'Encanada até a moradia'),
        ('encanada_cisterna', 'Encanada até a cisterna'),
        ('nao_encanada', 'Não encanada'),
        ('outros', 'Outros'),
    ]

    distribuicao_agua = models.CharField(max_length=100, verbose_name="Distribuição de água", blank=True, null=True)

    ABASTECIMENTO_ENERGIA_CHOICES = [
        ('rede_geral', 'Rede geral'),
        ('gerador', 'Gerador'),
        ('placa_solar', 'Placa solar'),
        ('outros', 'Outros'),
    ]
    abastecimento_energia = models.CharField(max_length=20, choices=ABASTECIMENTO_ENERGIA_CHOICES, verbose_name="Abastecimento de energia", blank=True, null=True)

    CHEGA_ENERGIA_INTERNET_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    chega_energia_internet = models.CharField(max_length=3, choices=CHEGA_ENERGIA_INTERNET_CHOICES, verbose_name="Chega energia/internet?", blank=True, null=True)

    ESGOTO_CHOICES = [
    ('Rede geral de esgoto', 'Rede geral de esgoto'),
    ('Fossa séptica', 'Fossa séptica'),
    ('Fossa rudimentar', 'Fossa rudimentar'),
    ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
    ('Vala', 'Vala'),
    ('Outro', 'Outro'),
    ]

    esgoto = models.CharField(max_length=100, choices=ESGOTO_CHOICES, verbose_name="Esgoto", blank=True, null=True)

    DESTINO_LIXO_CHOICES = [
        ('coleta_seletiva', 'Coleta seletiva'),
        ('coleta_regular', 'Coleta regular'),
        ('queima', 'Queima'),
        ('entulho', 'Entulho'),
        ('lixo_vivo', 'Lixo vivo'),
        ('outros', 'Outros'),
    ]

    lixo = models.CharField(max_length=100, choices=DESTINO_LIXO_CHOICES, verbose_name="Destino do lixo", blank=True, null=True)

    quantidade_comodos = models.IntegerField(verbose_name="Quantidade de cômodos", blank=True, null=True, validators=[MaxValueValidator(20)])

    quantidade_dormitorios = models.IntegerField(verbose_name="Quantidade de dormitórios", blank=True, null=True, validators=[MaxValueValidator(20)])

    banheiros = models.IntegerField(verbose_name="Quantidade de banheiros", blank=True, null=True, validators=[MaxValueValidator(20)])

    def __str__(self):
        return f"{self.endereco} - {self.nr_casa}"


class Morador(models.Model):
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='moradores')

    nome = models.CharField(max_length=50, verbose_name="Nome do morador", blank=True, null=True)
    sobrenome = models.CharField(max_length=200, verbose_name="Sobrenome do morador", blank=True, null=True)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo", blank=True, null=True)

    data_nascimento = models.DateField(verbose_name="Data de nascimento", blank=True, null=True)

    REGISTRO_NASCIMENTO_CHOICES = [
        ('do_cartorio', 'Do cartório'),
        ('registro_administrativo_de_nascimento_indígena', 'Registro administrativo de nascimento indígena'),
        ('nao_tem', 'Não tem'),
        ('nao_sabe', 'Não sabe'),
    ]
    registro_de_nascimento = models.CharField(max_length=100, choices=REGISTRO_NASCIMENTO_CHOICES, verbose_name="Tem registro de nascimento?", blank=True, null=True)

    RELACAO_RESPONSAVEL_CHOICES = [
        ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicilio'),
        ('conjuge_ou_companheiro(a)_de_sexo_diferente', 'Cônjuge ou companheiro(a) de sexo diferente'),
        ('conjuge_ou_companheiro(a)_do_mesmo_sexo', 'Cônjuge ou companheiro(a) do mesmo sexo'),
        ('filho(a)_do_responsavel_e_do_conjuge', 'Filho(a) do responsável e do cônjuge'),
        ('filho(a)_somente_do_responsavel', 'Filho(a) somente do responsável'),
        ('genro_ou_nora', 'Genro ou nora'),
        ('pai_mae_padrasto_ou_madrasta', 'Pai, mãe, padrasto ou madrasta'),
        ('sogro(a)', 'Sogro(a)'),
        ('neto(a)', 'Neto(a)'),
        ('enteado(a)', 'Enteado(a)'),
        ('irmao_ou_irma', 'Irmão ou irmã'),
        ('avo_ou_avo', 'Avô ou avó'),
        ('outroparente', 'Outro parente'),
        ('agregado(a)', 'Agregado(a)'),
        ('bisneto(a)', 'Bisneto(a)'),
        ('pensionista', 'Pensionista'),
        ('empregado(a)_domestico(a)', 'Empregado(a) doméstico(a)'),
        ('parente_do(a)_empregado(a)_domestico(a)', 'Parente do(a) empregado(a) doméstico(a)'),
        ('individual_em_domicilio_coletivo', 'Individual em domicílio coletivo'),
    ]
    relacao_com_responsavel = models.CharField(max_length=100, choices=RELACAO_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável pelo domicílio", blank=True, null=True)

    RELIGIAO_CHOICES = [
        ('cristianismo', 'Cristianismo'),
        ('islamismo', 'Islamismo'),
        ('hinduismo', 'Hinduísmo'),
        ('budismo', 'Budismo'),
        ('judaismo', 'Judaísmo'),
        ('espiritismo', 'Espiritismo'),
        ('outros', 'Outros'),
    ]
    religiao_ou_culto = models.CharField(max_length=50, choices=RELIGIAO_CHOICES, verbose_name="Religião ou culto", blank=True, null=True)

    SABE_LER_ESCREVER_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    sabe_ler_escrever = models.CharField(max_length=3, choices=SABE_LER_ESCREVER_CHOICES, verbose_name="Sabe ler e escrever?", blank=True, null=True)

    FREQUENTA_ESCOLA_CHOICES = [
        ('sim', 'Sim'),
        ('nao_ja_frequentou', 'Não, mas já frequentou'),
        ('nao_nunca_frequentou', 'Não, nunca frequentou'),
    ]
    frequenta_escola = models.CharField(max_length=25, choices=FREQUENTA_ESCOLA_CHOICES, verbose_name="Frequenta escola ou creche?", blank=True, null=True)

    CURSO_ATUAL_CHOICES = [
        ('pre_escola', 'pré-escola'),
        ('creche', 'creche'),
        ('alfabetizacao_adultos', 'Alfabetização de jovens e adultos'),
        ('ensino_fundamental', 'Regular do ensino fundamental'),
        ('eja_fundamental', 'Educação de jovens e adultos (eja) do ensino fundamental'),
        ('ensino_medio', 'Regular do ensino médio'),
        ('superior_graduacao', 'Superior de graduação'),
        ('eja_medio', 'Educação de jovens e adultos (eja) do ensino médio'),
        ('especializacao', 'Especialização de nível superior (duração mínima de 360 horas)'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
        ('nenhum', 'Nenhum'),
    ]
    curso_atual = models.CharField(max_length=25, choices=CURSO_ATUAL_CHOICES, verbose_name="Qual é o curso que frequenta?", blank=True, null=True)

    JA_CONCLUIU_SUPERIOR_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    ja_concluiu_curso_superior = models.CharField(max_length=3, choices=JA_CONCLUIU_SUPERIOR_CHOICES, verbose_name="Já concluiu algum outro curso superior de graduação?", blank=True, null=True)

    FAIXA_RENDIMENTO_CHOICES = [
        ('faixa_1_ate_500', '1 - 1,00 a 500,00'),
        ('faixa_2_501_a_1000', '2 - 501,00 a 1.000,00'),
        ('faixa_3_1001_a_2000', '3 - 1.001,00 a 2.000,00'),
        ('faixa_4_2001_a_3000', '4 - 2.001,00 a 3.000,00'),
        ('faixa_5_3001_a_5000', '5 - 3.001,00 a 5.000,00'),
        ('faixa_6_5001_a_10000', '6 - 5.001,00 a 10.000,00'),
        ('faixa_7_10001_a_20000', '7 - 10.001,00 a 20.000,00'),
        ('faixa_8_20001_a_100000', '8 - 20.001,00 a 100.000,00'),
        ('faixa_9_mais_de_100000', '9 - 100.001 ou mais'),
    ]
    faixa_de_rendimento = models.CharField(max_length=25, choices=FAIXA_RENDIMENTO_CHOICES, verbose_name="Faixa de rendimento", blank=True, null=True)

    DIAGNOSTICO_AUTISMO_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    diagnostico_autismo = models.CharField(max_length=3, choices=DIAGNOSTICO_AUTISMO_CHOICES, verbose_name="Já foi diagnosticado(a) com autismo por algum profissional de saúde?", blank=True, null=True)

    DIFICULDADE_ANDAR_CHOICES = [
        ('muita_dificuldade', 'Tem muita dificuldade'),
        ('nao_consegue', 'Tem, não consegue de modo algum'),
        ('alguma_dificuldade', 'Tem alguma dificuldade'),
        ('nao_tem_dificuldade', 'Não tem dificuldade'),
    ]
    dificuldade_andar = models.CharField(max_length=25, choices=DIFICULDADE_ANDAR_CHOICES, verbose_name="Tem dificuldade permanente para andar ou subir degraus, mesmo usando prótese, bengala ou aparelho de auxílio?", blank=True, null=True)

    DIFICULDADE_ENXERGAR_CHOICES = [
        ('nao_consegue', 'Tem, não consegue de modo algum'),
        ('muita_dificuldade', 'Tem muita dificuldade'),
        ('alguma_dificuldade', 'Tem alguma dificuldade'),
        ('nao_tem_dificuldade', 'Não tem dificuldade'),
    ]
    dificuldade_enxergar = models.CharField(max_length=25, choices=DIFICULDADE_ENXERGAR_CHOICES, verbose_name="Tem dificuldade permanente para enxergar, mesmo usando óculos ou lentes de contato?", blank=True, null=True)

    TRABALHOU_OU_ESTAGIOU_CHOICES = [
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    ]
    trabalhou_ou_estagiou = models.CharField(max_length=3, choices=TRABALHOU_OU_ESTAGIOU_CHOICES, verbose_name="Trabalhou ou estagiou em alguma atividade remunerada em dinheiro?", blank=True, null=True)

    NUMERO_DE_TRABALHOS_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres_ou_mais', '3 ou mais'),
    ]
    numero_de_trabalhos = models.CharField(max_length=20, choices=NUMERO_DE_TRABALHOS_CHOICES, verbose_name="Quantos trabalhos tinha nos últimos meses?", blank=True, null=True)

    ocupacao_funcao = models.TextField(max_length=400, verbose_name="Qual era a ocupação, cargo ou função que tinha nesse trabalho?", blank=True, null=True)
    atividade_negocio = models.TextField(max_length=400, verbose_name="Qual era a principal atividade do negócio ou empresa em que tinha esse trabalho?", blank=True, null=True)

    CARTEIRA_ASSINADA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    carteira_assinada = models.CharField(max_length=3, choices=CARTEIRA_ASSINADA_CHOICES, verbose_name="Nesse trabalho tinha carteira de trabalho assinada?", blank=True, null=True)

    EMPRESA_COM_CNPJ_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    empresa_com_cnpj = models.CharField(max_length=3, choices=EMPRESA_COM_CNPJ_CHOICES, verbose_name="Esse negócio ou empresa era registrado no cadastro nacional de pessoa jurídica - cnpj?", blank=True, null=True)

    MEIO_TRANSPORTE_TRABALHO_CHOICES = [
        ('a_pe', 'A pé'),
        ('bicicleta', 'Bicicleta'),
        ('motocicleta', 'Motocicleta'),
        ('mototaxi', 'Mototáxi'),
        ('automovel', 'Automóvel'),
        ('taxi', 'Táxi ou assemelhados'),
        ('van', 'Van, perua ou assemelhados'),
        ('onibus', 'Ônibus'),
        ('pau_de_arara', 'Caminhonete ou caminhão adaptado (pau de arara)'),
        ('embarcacao_grande', 'Embarcação de médio e grande porte (acima de 20 pessoas)'),
        ('embarcacao_pequena', 'Embarcação de pequeno porte (até 20 pessoas)'),
        ('outros', 'Outros'),
    ]
    meio_transporte_trabalho = models.CharField(max_length=25, choices=MEIO_TRANSPORTE_TRABALHO_CHOICES, verbose_name="Qual o principal meio de transporte utilizado para chegar ao local de trabalho? (Se utiliza vários meios de transporte, inclusive a pé, indique o que passa mais tempo.)", blank=True, null=True)

    TEMPO_CASA_TRABALHO_CHOICES = [
        ('10', 'até 10 minutos'),
        ('15', 'até 15 minutos'),
        ('30', 'até 30 minutos'),
        ('45', 'até 45 minutos'),
        ('1h', 'até 1 hora'),
        ('1+', '1h+'),
        ('nao_desloca', 'Não se desloca para um local de trabalho'),
    ]
    tempo_casa_trabalho = models.CharField(max_length=25, choices=TEMPO_CASA_TRABALHO_CHOICES, verbose_name="Quanto tempo leva entre sua casa e o local de trabalho normalmente?(Considerar o deslocamento casa-trabalho preferencialmente. Caso não seja possível, considerar o deslocamento de retorno (trabalho-casa))", blank=True, null=True)

    ONDE_TRABALHA_CHOICES = [
        ('em_casa_ou_propriedade', 'Apenas em casa ou na propriedade/neste município'),
        ('fora_casa_propriedade', 'Fora de casa e da propriedade/neste município'),
        ('outro_municipio', 'Em outro município do Brasil'),
        ('outro_pais', 'Em outro país'),
        ('mais_de_um_local', 'Em mais de um município ou país'),
    ]
    onde_trabalha = models.CharField(max_length=25, choices=ONDE_TRABALHA_CHOICES, verbose_name="Em que município ou país estrangeiro trabalha?", blank=True, null=True)

    estado_trabalho = models.CharField(max_length=25, verbose_name="Estado", blank=True, null=True)
    municipio_trabalho = models.CharField(max_length=25, verbose_name="Município", blank=True, null=True)
    pais_trabalho = models.CharField(max_length=25, verbose_name="País", blank=True, null=True)

    RETORNA_3X_SEMANA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    retorna_3x_semana = models.CharField(max_length=3, choices=RETORNA_3X_SEMANA_CHOICES, verbose_name="Retorna do trabalho para casa 3 dias ou mais na semana? (considerar a semana de 7 dias)", blank=True, null=True)

    NUPCIALIDADE_CHOICES = [
        ('possui_conjuge_ou_companheiro(a)', 'Possui conjuge ou companheiro(a)'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    nupcialidade = models.CharField(max_length=50, choices=NUPCIALIDADE_CHOICES, verbose_name="Nupcialidade", blank=True, null=True)

    VIVE_EM_COMPANHIA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    vive_em_companhia = models.CharField(max_length=3, choices=VIVE_EM_COMPANHIA_CHOICES, verbose_name="Vivem com companhia de conjuge ou companheiro(a)?", blank=True, null=True)

    nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do cônjuge", blank=True, null=True)

    TIPO_UNIAO_CHOICES = [
        ('casamento_civil_e_religioso', 'Casamento civil e religioso'),
        ('so_casamento_civil', 'So casamento civil'),
        ('so_casamento_religioso', 'So casamento religioso'),
        ('uniao_consensual', 'União consensual'),
    ]
    tipo_uniao = models.CharField(max_length=50, choices=TIPO_UNIAO_CHOICES, verbose_name="Tipo de união", blank=True, null=True)

    FALECEU_ALGUEM_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    faleceu_alguem = models.CharField(max_length=3, choices=FALECEU_ALGUEM_CHOICES, verbose_name="Faleceu alguma pessoa que morava com você(s)? (inclusive recém-nascidos e idosos)", blank=True, null=True)

    nome_falecido = models.CharField(max_length=50, verbose_name="Nome do falecido", blank=True, null=True)
    sobrenome_falecido = models.CharField(max_length=50, verbose_name="Sobrenome do falecido", blank=True, null=True)

    SEXO_FALECIDO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]
    sexo_falecido = models.CharField(max_length=1, choices=SEXO_FALECIDO_CHOICES, verbose_name="Sexo do falecido", blank=True, null=True)

    idade_falecido = models.IntegerField(verbose_name="Quantos anos tinha ao falecer?", blank=True, null=True, validators=[MaxValueValidator(120)])
    data_falecimento = models.DateField(verbose_name="Mês e ano de falecimento", blank=True, null=True)

    nome_contato = models.CharField(max_length=25, verbose_name="Nome do contato", blank=True, null=True)
    email_contato = models.CharField(max_length=25, verbose_name="E-mail do contato", blank=True, null=True)
    telefone_contato = models.CharField(max_length=25, verbose_name="Telefone do contato", blank=True, null=True)

    def __str__(self):
        return self.nome if self.nome else "Morador" + (self.sobrenome if self.sobrenome else "")
