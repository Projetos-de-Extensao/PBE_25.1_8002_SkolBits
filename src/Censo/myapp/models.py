from django.db import models

#inicio da troca
class IndentificacaoDeDomicilio(models.Model):

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

class InformacoesMoradores(models.Model):
    QTD_MORADORES_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres', '3'),
        ('quatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
        ('sete_ou_mais', '7+'),
    ]
    quantidade_moradores = models.CharField(max_length=12, choices=QTD_MORADORES_CHOICES, verbose_name="Quantidade de moradores", blank=True, null=True)

    nome_completo = models.CharField(max_length=50, verbose_name="Nome completo", null=True, blank=True)

    data_nascimento = models.DateField(verbose_name="Data de nascimento", null=True, blank=True)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo", blank=True, null=True)
    
    RELACAO_COM_RESPONSAVEL_CHOICES = [
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
        ('outros', 'Outros'),
    ]
    relacao_com_responsavel = models.CharField(max_length=100, choices=RELACAO_COM_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável pelo domicílio", blank=True, null=True)

    CONDIÇÃO_POSSE_CHOICES = [
        ('pagando', 'Ainda pagando'),
        ('alugada', 'Alugada'),
        ('por_empregador', 'Por empregador'),
        ('por_familiar', 'Por familiar'),
        ('outra_forma', 'Outra forma'),
        ('outra_condicao', 'Outra condição'),
        ('ja_pago', 'Já pago, herdado ou ganho'),
    ]
    condicao_posse = models.CharField(max_length=50, choices=CONDIÇÃO_POSSE_CHOICES, verbose_name="Condição de posse do domicílio", blank=True, null=True)



class CaracteristicasDomicilio(models.Model):
    QUANTIDADE_COMODOS_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres', '3'),
        ('quatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
        ('sete_ou_mais', '7+'),
    ]
    quantidade_comodos = models.CharField(max_length=12, choices=QUANTIDADE_COMODOS_CHOICES, verbose_name="Quantidade de cômodos", blank=True, null=True)

    QUANTIDADE_DORMITORIOS_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres', '3'),
        ('quatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
        ('sete_ou_mais', '7+'),
    ]
    quantidade_dormitorios = models.CharField(max_length=12, choices=QUANTIDADE_DORMITORIOS_CHOICES, verbose_name="Quantidade de dormitórios", blank=True, null=True)

    QUANTIDADE_BANHEIROS_COM_CHUVEIRO_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres', '3'),
        ('quatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
        ('sete_ou_mais', '7+'),
    ]
    quantidade_banheiro_com_chuveiro = models.CharField(max_length=12, choices=QUANTIDADE_BANHEIROS_COM_CHUVEIRO_CHOICES, verbose_name="Quantidade de banheiros", blank=True, null=True)

    QUANTIDADE_BANHEIROS_SEM_CHUVEIRO_CHOICES = [
        ('um', '1'),
        ('dois', '2'),
        ('tres', '3'),
        ('quatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
        ('sete_ou_mais', '7+'),
    ]
    quantidade_banheiro_sem_chuveiro = models.CharField(max_length=12, choices=QUANTIDADE_BANHEIROS_SEM_CHUVEIRO_CHOICES, verbose_name="Quantidade de banheiros", blank=True, null=True)

    TEM__INTERNET_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    tem_internet = models.CharField(max_length=3, choices=TEM__INTERNET_CHOICES, verbose_name="Tem internet?", blank=True, null=True)

    MAQUINA_LAVAR = [  
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    maquina_lavar = models.CharField(max_length=3, choices=MAQUINA_LAVAR, verbose_name="Tem máquina de lavar?", blank=True, null=True)
    

class RegistroCivil(models.Model):
    REGISTRO_NASCIMENTO_CHOICES = [
        ('do_cartorio', 'Do cartório'),
        ('nao_tem', 'Não tem'),
        ('nao_sabe', 'Não sabe'),
    ]
    registro_nascimento = models.CharField(max_length=12, choices=REGISTRO_NASCIMENTO_CHOICES, verbose_name="Registro de nascimento", blank=True, null=True)

class Nupcialidade(models.Model):
   
    POSSUI_CONJUGE_CHOICES = [
        ('s', 'Sim'),
        ('n', 'Não'),
    ]
    possui_conjuge = models.CharField(max_length=1, choices=POSSUI_CONJUGE_CHOICES, blank=True, null=True)

    VIVE_EM_COMPANHIA_CHOICES= [
        ('s', 'Sim'),
        ('n', 'Não'),
    ]
    vive_em_companhia = models.CharField(max_length=1, choices=VIVE_EM_COMPANHIA_CHOICES, verbose_name="Vive em companhia de cônjuge ou companheiro(a)?", blank=True, null=True)

    nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do cônjuge", blank=True, null=True)

    TIPO_UNIAO_CHOICES = [
        ('casamento_civil_e_religioso', 'Casamento civil e religioso'),
        ('so_casamento_civil', 'So casamento civil'),
        ('so_casamento_religioso', 'So casamento religioso'),
        ('uniao_consensual', 'União consensual'),
    ]
    tipo_uniao = models.CharField(max_length=50, choices=TIPO_UNIAO_CHOICES, verbose_name="Tipo de união", blank=True, null=True)

class TrabalhoErendimento(models.Model):
    TRABALHOU_OU_ESTAGIOU_CHOICES = [
        ("sim", "Sim"),
        ("nao", "Não"),
    ]
    trabalhou_ou_estagiou = models.CharField(max_length=3, choices=TRABALHOU_OU_ESTAGIOU_CHOICES, verbose_name="Trabalhou ou estagiou em alguma atividade remunerada em dinheiro?", blank=True, null=True)

    NUMERO_DE_TRABALHOS_ULTIMOS_MESES_CHOICES = [
        ("um", "1"),
        ("dois", "2"),
        ("tres_ou_mais", "3 ou mais"),
    ]
    numero_de_trabalhos = models.CharField(max_length=20, choices=NUMERO_DE_TRABALHOS_ULTIMOS_MESES_CHOICES, verbose_name="Quantos trabalhos tinha nos últimos meses?", blank=True, null=True)
    
    ocupacao_funcao = models.TextField(max_length=400, verbose_name="Qual era a ocupação, cargo ou função que tinha nesse trabalho?", blank=True, null=True)

    atividade_negocio = models.TextField(max_length=400, verbose_name="Qual era a principal atividade do negócio ou empresa em que tinha esse trabalho?", blank=True, null=True)
    
    CARTEIRA_ASSINADA_CHOICES = [
        ("sim", "Sim"),
        ("nao", "Não"),
    ]
    carteira_assinada = models.CharField(max_length=3, choices=CARTEIRA_ASSINADA_CHOICES, verbose_name="Nesse trabalho tinha carteira de trabalho assinada?", blank=True, null=True)

    EMPRESA_COM_CNPJ_CHOICES = [
        ("sim", "Sim"),
        ("nao", "Não"),
    ]
    empresa_com_cnpj = models.CharField(max_length=3, choices=EMPRESA_COM_CNPJ_CHOICES, verbose_name="Esse negócio ou empresa era registrado no cadastro nacional de pessoa jurídica - cnpj?", blank=True, null=True)

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
    faixa_de_rendimento = models.CharField(max_length=25, choices=FAIXA_DE_RENDIMENTO_CHOICES, verbose_name="Faixa de rendimento", blank=True, null=True)

class Taxa_mortalidade(models.Model):
    FALECEU_ALGUEM_CHOICES = [
        ("sim", "Sim"),
        ("nao", "Não"),
    ]
    faleceu_alguem = models.CharField(max_length=3, choices=FALECEU_ALGUEM_CHOICES, verbose_name="Faleceu alguma pessoa que morava com você(s)? (inclusive recém-nascidos e idosos)", blank=True, null=True)

    data_falecimento = models.DateField(verbose_name="Mês e ano de falecimento", blank=True, null=True)

    nome_completo_falecido = models.CharField(max_length=200, verbose_name="Nome completo do falecido", blank=True, null=True)
    idade_falecido = models.IntegerField(verbose_name="Idade do falecido", blank=True, null=True)

    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outros"),
    ]
    sexo_falecido = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo do falecido", blank=True, null=True)


class PessoaComDeficiencia(models.Model):
    DIFICULDADE_ENXERGAR_CHOICES = [
        ("nao_consegue", "Tem, não consegue de modo algum"),
        ("muita_dificuldade", "Tem muita dificuldade"),
        ("alguma_dificuldade", "Tem alguma dificuldade"),
        ("nao_tem_dificuldade", "Não tem dificuldade"),
    ]
    dificuldade_enxergar = models.CharField(
        max_length=25,
        choices=DIFICULDADE_ENXERGAR_CHOICES,
        verbose_name="tem dificuldade permanente para enxergar, mesmo usando óculos ou lentes de contato?",
        blank=True,
        null=True
    )
    DIFICULDADE_OUVIR_CHOICES = [
        ("nao_consegue", "Tem, não consegue de modo algum"),
        ("muita_dificuldade", "Tem muita dificuldade"),
        ("alguma_dificuldade", "Tem alguma dificuldade"),
        ("nao_tem_dificuldade", "Não tem dificuldade"),
    ]
    dificuldade_ouvir = models.CharField(
        max_length=25,
        choices=DIFICULDADE_OUVIR_CHOICES,
        verbose_name="tem dificuldade permanente para ouvir, mesmo usando aparelho auditivo?",
        blank=True,
        null=True
    )
    DIFICULDADE_PERMANENTE_ANDAR_CHOICES = [
        ("nao_consegue", "Tem, não consegue de modo algum"),
        ("muita_dificuldade", "Tem muita dificuldade"),
        ("alguma_dificuldade", "Tem alguma dificuldade"),
        ("nao_tem_dificuldade", "Não tem dificuldade"),
    ]
    dificuldade_permanente_andar = models.CharField(
        max_length=25,
        choices=DIFICULDADE_PERMANENTE_ANDAR_CHOICES,
        verbose_name="tem dificuldade permanente para andar ou subir escadas?",
        blank=True,
        null=True
    )

class Educacao(models.Model):
    QUANTAS_PESSOAS_LER_ESCRE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7_ou_mais', '7 ou mais'),
    ]
    quantas_pessoas_ler_escre = models.CharField(
        max_length=12,
        choices=QUANTAS_PESSOAS_LER_ESCRE_CHOICES,
        verbose_name="Quantas pessoas sabem ler e escrever?",
        blank=True,
        null=True
    )
    FREQUENTA_ESCOLA_CRECHE_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'mas já frequentou'),
        ('nao', 'Nunca frequentou'),
    ]
    frequenta_escola_creche = models.CharField(
        max_length=3,
        choices=FREQUENTA_ESCOLA_CRECHE_CHOICES,
        verbose_name="Algum morador frequenta escola ou creche?",
        blank=True,
        null=True
    )
    CURSO_ATUAL_CHOICES = [
        ("pre_escola", "pré-escola"),
        ("creche", "creche"),
        ("alfabetizacao_adultos", "Alfabetização de jovens e adultos"),
        ("ensino_fundamental", "Regular do ensino fundamental"),
        ("eja_fundamental", "Educação de jovens e adultos (eja) do ensino fundamental"),
        ("ensino_medio", "Regular do ensino médio"),
        ("superior_graduacao", "Superior de graduação"),
        ("eja_medio", "Educação de jovens e adultos (eja) do ensino médio"),
        ("especializacao", "Especialização de nível superior (duração mínima de 360 horas)"),
        ("mestrado", "Mestrado"),
        ("doutorado", "Doutorado"),
        ("nenhum", "Nenhum"),
    ]
    curso_atual = models.CharField(
        max_length=25,
          choices=CURSO_ATUAL_CHOICES, 
          verbose_name="Qual é o curso que frequenta?", blank=True, null=True
    )      
    JA_CONCLUIU_CURSO_SUPERIOR_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    ja_concluiu_curso_superior = models.CharField(
        max_length=3,
        choices=JA_CONCLUIU_CURSO_SUPERIOR_CHOICES,
        verbose_name="Já concluiu curso superior?",
        blank=True,
        null=True
    )
    
class DeslocamentoParaTrabalho(models.Model):
    ALGUM_MORADOR_TRABALHA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    algum_morador_trabalha = models.CharField(
        max_length=3,
        choices=ALGUM_MORADOR_TRABALHA_CHOICES,
        verbose_name="Algum morador trabalha?",
        blank=True,
        null=True
    )  

    MUNICIPIO_OU_PAIS_TRABALHA = [
        ('Apenas em casa ou na propriedade/municipio', 'Apenas em casa ou na propriedade/neste municipio'),
        ('Fora de casa e da propriedade/municipio', 'Fora de casa e da propriedade/neste municipio'),
        ('Em outro municipio do Brasil', 'Em outro município do Brasil'),
        ('Em outro pais', 'Em outro pais'),
        ('Em mais de um municipio ou pais', 'Em mais de um município ou pais'),
    ]
    MUNICIPIO_OU_PAIS_TRABALHA = models.CharField(
        max_length=100,
        choices=MUNICIPIO_OU_PAIS_TRABALHA,
        verbose_name="Em que município ou país trabalha?",
        blank=True,
        null=True
    )
    RETORNA_DO_TRABALHO_PARA_CASA = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    retorna_do_trabaho_pra_casa = models.CharField(
        max_length=3,
        choices=RETORNA_DO_TRABALHO_PARA_CASA,
        verbose_name="Retorna do trabalho para casa?",
        blank=True,
        null=True
    )
    TEMPO_CASA_TRABALHO_CHOICES = (
    [(str(horas), f"{horas} hora(s)") for horas in range(0, 25)] +
    [(str(minutos), f"{minutos} minuto(s)") for minutos in range(0, 60)] +
    [("nao_desloca", "Não se desloca para um local de trabalho")]
    )
    tempo_casa_trabalho = models.CharField(max_length=25, choices=TEMPO_CASA_TRABALHO_CHOICES, verbose_name="Quanto tempo leva entre sua casa e o local de trabalho normalmente?(Considerar o deslocamento casa-trabalho preferencialmente. Caso não seja possível, considerar o deslocamento de retorno (trabalho-casa))", blank=True, null=True)

    MEIO_TRANSPORTE_TRABALHO_CHOICES = [
        ("a_pe", "A pé"),
        ("bicicleta", "Bicicleta"),
        ("motocicleta", "Motocicleta"),
        ("mototaxi", "Mototáxi"),
        ("automovel", "Automóvel"),
        ("taxi", "Táxi ou assemelhados"),
        ("van", "Van, perua ou assemelhados"),
        ("onibus", "Ônibus"),
        ("pau_de_arara", "Caminhonete ou caminhão adaptado (pau de arara)"),
        ("embarcacao_grande", "Embarcação de médio e grande porte (acima de 20 pessoas)"),
        ("embarcacao_pequena", "Embarcação de pequeno porte (até 20 pessoas)"),
        ("outros", "Outros"),
    ]
    meio_transporte_trabalho = models.CharField(max_length=25, choices=MEIO_TRANSPORTE_TRABALHO_CHOICES, verbose_name="Qual o principal meio de transporte utilizado para chegar ao local de trabalho? (Se utiliza vários meios de transporte, inclusive a pé, indique o que passa mais tempo.)", blank=True, null=True)

    

#fim da troca 

# class Domicilio(models.Model):


#     TIPO_CHOICES = [
#         ('casa', 'Casa'),
#         ('casa_vila_ou_condominio', 'Casa de vila ou em condomínio'),
#         ('casa_comodos_ou_cortiço', 'Habitação em casa de cômodos ou cortiço'),
#         ('estrututura_degradada_ou_inacabada', 'Estrutura não residencial permanente degradada ou inacabada'),
#         ('asilo', 'Asilo ou outra instrituição de longa permanência'),
#         ("hotel_ou_pensao", 'Hotel ou pensão'),
#         ('alojamento', 'Alojamento'),
#         ('outros', 'Outros'),
#     ]
#     tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de domicílio", blank=True, null=True)

#     CONDIÇÃO_POSSE_CHOICES = [
#         ('pagando', 'Ainda pagando'),
#         ('alugada', 'Alugada'),
#         ('por_empregador', 'Por empregador'),
#         ('por_familiar', 'Por familiar'),
#         ('outra_forma', 'Outra forma'),
#         ('outra_condicao', 'Outra condição'),
#         ('ja_pago', 'Já pago, herdado ou ganho'),
#     ]
#     condicao_posse = models.CharField(max_length=50, choices=CONDIÇÃO_POSSE_CHOICES, verbose_name="Condição de posse do domicílio", blank=True, null=True)

#     ABASTECIMENTO_AGUA_CHOICES = [
#         ('rede_geral', 'Rede geral de distribuição'),
#         ('poco_artesiano', 'Poço artesiano'),
#         ('cacimba', 'Cacimba'),
#         ('rio_lago_corregos_ou_represas', 'Rio, lago, córregos ou represas'),
#         ('fonte_nascente_ou_mina', 'fonte, nascente ou mina'),
#         ('carro-pipa', 'carro-pipa'),
#         ('agua_de_chuva', 'água de chuva'),
#         ('outro', 'Outro'),
#     ]
#     abastecimento_agua = models.CharField(max_length=50, choices=ABASTECIMENTO_AGUA_CHOICES, verbose_name="Abastecimento de água", blank=True, null=True)

#     DISTRIBUICAO_AGUA_CHOICES = [
#         ('Encanada até dentro da moradia', 'Encanada até dentro da moradia'),
#         ('Encanada, mas apenas terreno ou quintal', 'Encanada, mas apenas terreno ou quintal'),
#         ('Não encanada', 'Não encanada'),
#     ]
#     distribuicao_agua = models.CharField(max_length=50, choices=DISTRIBUICAO_AGUA_CHOICES, verbose_name="Distribuição de água", blank=True, null=True)
    
#     ABASTECIMENTO_ENERGIA_CHOICES = [
#         ('rede_geral', 'Rede geral de distribuição'),
#         ('gerador', 'Gerador'),
#         ('energia_solar', 'Energia solar'),
#         ('energia_eolica', 'Energia eólica'),
#         ('energia_hidraulica', 'Energia hidráulica'),
#         ('outra_fonte', 'Outra fonte'),
#     ]
#     abastecimento_energia = models.CharField(max_length=50, choices=ABASTECIMENTO_ENERGIA_CHOICES, verbose_name="Abastecimento de energia", blank=True, null=True)

#     CHEGA_ENERGIA_INTERNET_CHOICES = [
#         ('sim', 'Sim'),
#         ('nao', 'Não'),
#     ]
#     chega_energia_internet = models.CharField(max_length=3, choices=CHEGA_ENERGIA_INTERNET_CHOICES, verbose_name="Chega energia e internet?", blank=True, null=True)
    
#     ESGOTO_CHOICES = [
#         ('Rede geral de esgoto', 'Rede geral de esgoto'),
#         ('Fossa séptica', 'Fossa séptica'),
#         ('Fossa rudimentar', 'Fossa rudimentar'),
#         ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
#         ('Vala', 'Vala'),
#         ('Outro', 'Outro'),
#     ]
#     esgoto = models.CharField(max_length=50, choices=ESGOTO_CHOICES, verbose_name="Esgoto", blank=True, null=True)

#     LIXO_CHOICES = [
#         ('coletado_prefeitura', 'Coletado pela prefeitura'),
#         ('coletado_empresa', 'Coletado por empresa particular'),
#         ('queimado', 'Queimado'),
#         ('enterrado', 'Enterrado'),
#         ('jogado_terreno_baldio', 'Jogado em terreno baldio'),
#         ('jogado_rio_lago_corrego_represa', 'Jogado em rio, lago, córrego ou represa'),
#         ('outro', 'Outro'),
#     ]
#     lixo = models.CharField(max_length=50, choices=LIXO_CHOICES, verbose_name="Destinação do lixo", blank=True, null=True)

#     quantidade_comodos = models.IntegerField(verbose_name="Quantidade de cômodos", null=True, blank=True)
#     quantidade_dormitorios = models.IntegerField(verbose_name="Quantidade de dormitórios", null=True, blank=True)
#     banheiros = models.IntegerField(verbose_name="Banheiros", null=True, blank=True)

# class Morador (models.Model):
#     nome = models.CharField(max_length=50, verbose_name="Nome do morador", null=True, blank=True)
#     sobrenome = models.CharField(max_length=200, verbose_name="Sobrenome do morador", null=True, blank=True)

#     SEXO_CHOICES = [
#         ('M', 'Masculino'),
#         ('F', 'Feminino'),
#     ]
#     sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo", blank=True, null=True)

#     data_nascimento = models.DateField(verbose_name="Data de nascimento", null=True, blank=True)

#     RELACAO_COM_RESPONSAVEL_CHOICES = [
#         ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicilio'),
#         ('conjuge_ou_companheiro(a)_de_sexo_diferente', 'Cônjuge ou companheiro(a) de sexo diferente'),
#         ('conjuge_ou_companheiro(a)_do_mesmo_sexo', 'Cônjuge ou companheiro(a) do mesmo sexo'),
#         ('filho(a)_do_responsavel_e_do_conjuge', 'Filho(a) do responsável e do cônjuge'),
#         ('filho(a)_somente_do_responsavel', 'Filho(a) somente do responsável'),
#         ('pessoa_responsavel_pelo_domicilio', 'Pessoa responsável pelo domicílio'),
#         ('genro_ou_nora', 'Genro ou nora'),
#         ('pai_mae_padrasto_ou_madrasta', 'Pai, mãe, padrasto ou madrasta'),
#         ('sogro(a)', 'Sogro(a)'),
#         ('neto(a)', 'Neto(a)'),
#         ('enteado(a)', 'Enteado(a)'),
#         ('irmão_ou_irma', 'Irmão ou irmã'),
#         ('avô_ou_avo', 'Avô ou avó'),
#         ('outroparente', 'Outro parente'),
#         ('agregado(a)', 'Agregado(a)'),
#         ('bisneto(a)', 'Bisneto(a)'),
#         ('pensionista', 'Pensionista'),
#         ('empregado(a)_domestico(a)', 'Empregado(a) doméstico(a)'),
#         ('parente_do(a)_empregado(a)_domestico(a)', 'Parente do(a) empregado(a) doméstico(a)'),
#         ('individual_em_domicilio_coletivo', 'Individual em domicílio coletivo'),
#     ]
#     relacao_com_responsavel = models.CharField(max_length=100, choices=RELACAO_COM_RESPONSAVEL_CHOICES, verbose_name="Relação com responsável pelo domicílio", blank=True, null=True)

#     REGISTRO_DE_NASCIMENTO_CHOICES = [
#         ('do_cartorio', 'Do cartório'),
#         ('registro_administrativo_de_nascimento_indígena', 'Registro administrativo de nascimento indígena'),
#         ('nao_tem', 'Não tem'),
#         ('nao_sabe', 'Não sabe'),
#     ]
#     registro_de_nascimento = models.CharField(max_length=100, choices=REGISTRO_DE_NASCIMENTO_CHOICES, verbose_name="Tem registro de nascimento?", blank=True, null=True)

#     NUPICIALIDADE_CHOICES = [
#         ('possui_conjuge_ou_companheiro(a)', 'Possui conjuge ou companheiro(a)'),
#         ('sim', 'Sim'),
#         ('nao', 'Não'),
#     ]
#     nupicialidade = models.CharField(max_length=50, choices=NUPICIALIDADE_CHOICES, verbose_name="Nupicialidade", blank=True, null=True)

#     VIVEM_COMPANHIA_CHOICES = [
#         ('sim', 'Sim'),
#         ('nao', 'Não'),
#     ]
#     vivem_companhia = models.CharField(max_length=3, choices=VIVEM_COMPANHIA_CHOICES, verbose_name="Vivem com companhia de conjuge ou companheiro(a)?", blank=True, null=True)

#     nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do cônjuge", blank=True, null=True)

#     TIPO_UNIAO_CHOICES = [
#         ('casamento_civil_e_religioso', 'Casamento civil e religioso'),
#         ('so_casamento_civil', 'So casamento civil'),
#         ('so_casamento_religioso', 'So casamento religioso'),
#         ('uniao_consensual', 'União consensual'),
#     ]
#     tipo_uniao = models.CharField(max_length=50, choices=TIPO_UNIAO_CHOICES, verbose_name="Tipo de união", blank=True, null=True)

#     TRABALHOU_OU_ESTAGIOU_CHOICES = [
#     ("SIM", "Sim"),
#     ("NAO", "Não"),
#     ]
#     trabalhou_ou_estagiou = models.CharField(max_length=3, choices=TRABALHOU_OU_ESTAGIOU_CHOICES, verbose_name="Trabalhou ou estagiou em alguma atividade remunerada em dinheiro?", blank=True, null=True)

#     NUMERO_DE_TRABALHOS_CHOICES = [
#     ("um", "1"),
#     ("dois", "2"),
#     ("tres_ou_mais", "3 ou mais"),
#     ]
#     numero_de_trabalhos = models.CharField(max_length=20, choices=NUMERO_DE_TRABALHOS_CHOICES, verbose_name="Quantos trabalhos tinha nos últimos meses?", blank=True, null=True)
    
#     ocupacao_funcao = models.TextField(max_length=400, verbose_name="Qual era a ocupação, cargo ou função que tinha nesse trabalho?", blank=True, null=True)

#     atividade_negocio = models.TextField(max_length=400, verbose_name="Qual era a principal atividade do negócio ou empresa em que tinha esse trabalho?", blank=True, null=True)
    
#     CARTEIRA_ASSINADA_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     carteira_assinada = models.CharField(max_length=3, choices=CARTEIRA_ASSINADA_CHOICES, verbose_name="Nesse trabalho tinha carteira de trabalho assinada?", blank=True, null=True)

#     EMPRESA_COM_CNPJ_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     empresa_com_cnpj = models.CharField(max_length=3, choices=EMPRESA_COM_CNPJ_CHOICES, verbose_name="Esse negócio ou empresa era registrado no cadastro nacional de pessoa jurídica - cnpj?", blank=True, null=True)

#     FAIXA_DE_RENDIMENTO_CHOICES = [
#     ("faixa_1_ate_500", "1 - 1,00 a 500,00"),
#     ("faixa_2_501_a_1000", "2 - 501,00 a 1.000,00"),
#     ("faixa_3_1001_a_2000", "3 - 1.001,00 a 2.000,00"),
#     ("faixa_4_2001_a_3000", "4 - 2.001,00 a 3.000,00"),
#     ("faixa_5_3001_a_5000", "5 - 3.001,00 a 5.000,00"),
#     ("faixa_6_5001_a_10000", "6 - 5.001,00 a 10.000,00"),
#     ("faixa_7_10001_a_20000", "7 - 10.001,00 a 20.000,00"),
#     ("faixa_8_20001_a_100000", "8 - 20.001,00 a 100.000,00"),
#     ("faixa_9_mais_de_100000", "9 - 100.001 ou mais"),
#     ]
#     faixa_de_rendimento = models.CharField(max_length=25, choices=FAIXA_DE_RENDIMENTO_CHOICES, verbose_name="Faixa de rendimento", blank=True, null=True)

#     FALECEU_ALGUEM_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     faleceu_alguem = models.CharField(max_length=3, choices=FALECEU_ALGUEM_CHOICES, verbose_name="Faleceu alguma pessoa que morava com você(s)? (inclusive recém-nascidos e idosos)", blank=True, null=True)

#     data_falecimento = models.DateField(verbose_name="Mês e ano de falecimento", blank=True, null=True)

#     nome_falecido = models.CharField(max_length=50, verbose_name="Nome do falecido", blank=True, null=True)
#     sobrenome_falecido = models.CharField(max_length=50, verbose_name="Sobrenome do falecido", blank=True, null=True)

#     SEXO_CHOICES = [
#     ("M", "Masculino"),
#     ("F", "Feminino"),
#     ("O", "Outros"),
#     ]
#     sexo_falecido = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo do falecido", blank=True, null=True)

#     idade_falecido = models.IntegerField(verbose_name="Quantos anos tinha ao falecer?", blank=True, null=True)

#     DIFICULDADE_ENXERGAR_CHOICES = [
#     ("nao_consegue", "Tem, não consegue de modo algum"),
#     ("muita_dificuldade", "Tem muita dificuldade"),
#     ("alguma_dificuldade", "Tem alguma dificuldade"),
#     ("nao_tem_dificuldade", "Não tem dificuldade"),
#     ]
#     dificuldade_enxergar = models.CharField(max_length=25, choices=DIFICULDADE_ENXERGAR_CHOICES, verbose_name="tem dificuldade permanente para enxergar, mesmo usando óculos ou lentes de contato?", blank=True, null=True)

#     DIFICULDADE_ANDAR_CHOICES = [
#     ("muita_dificuldade", "Tem muita dificuldade"),
#     ("nao_consegue", "Tem, não consegue de modo algum"),
#     ("alguma_dificuldade", "Tem alguma dificuldade"),
#     ("nao_tem_dificuldade", "Não tem dificuldade"),
#     ]
#     dificuldade_andar = models.CharField(max_length=25, choices=DIFICULDADE_ANDAR_CHOICES, verbose_name="Tem dificuldade permanente para andar ou subir degraus, mesmo usando prótese, bengala ou aparelho de auxílio?", blank=True, null=True)

#     SABE_LER_ESCREVER_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     sabe_ler_escrever = models.CharField(max_length=3, choices=SABE_LER_ESCREVER_CHOICES, verbose_name="Sabe ler e escrever?", blank=True, null=True)

#     FREQUENTA_ESCOLA_CHOICES = [
#     ("sim", "Sim"),
#     ("nao_ja_frequentou", "Não, mas já frequentou"),
#     ("nao_nunca_frequentou", "Não, nunca frequentou"),
#     ]
#     frequenta_escola = models.CharField(max_length=25, choices=FREQUENTA_ESCOLA_CHOICES, verbose_name="frequenta escola ou creche? (escola inclui desde cursos da pré-escola até o doutorado)", blank=True, null=True)

#     CURSO_ATUAL_CHOICES = [
#     ("pre_escola", "pré-escola"),
#     ("creche", "creche"),
#     ("alfabetizacao_adultos", "Alfabetização de jovens e adultos"),
#     ("ensino_fundamental", "Regular do ensino fundamental"),
#     ("eja_fundamental", "Educação de jovens e adultos (eja) do ensino fundamental"),
#     ("ensino_medio", "Regular do ensino médio"),
#     ("superior_graduacao", "Superior de graduação"),
#     ("eja_medio", "Educação de jovens e adultos (eja) do ensino médio"),
#     ("especializacao", "Especialização de nível superior (duração mínima de 360 horas)"),
#     ("mestrado", "Mestrado"),
#     ("doutorado", "Doutorado"),
#     ("nenhum", "Nenhum"),
#     ]
#     curso_atual = models.CharField(max_length=25, choices=CURSO_ATUAL_CHOICES, verbose_name="Qual é o curso que frequenta?", blank=True, null=True)

#     JA_CONCLUIU_CURSO_SUPERIOR_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     ja_concluiu_curso_superior = models.CharField(max_length=3, choices=JA_CONCLUIU_CURSO_SUPERIOR_CHOICES, verbose_name="Já concluiu algum outro curso superior de graduação?", blank=True, null=True)

#     ONDE_TRABALHA_CHOICES = [
#     ("em_casa_ou_propriedade", "Apenas em casa ou na propriedade/neste município"),
#     ("fora_casa_propriedade", "Fora de casa e da propriedade/neste município"),
#     ("outro_municipio", "Em outro município do Brasil"),
#     ("outro_pais", "Em outro país"),
#     ("mais_de_um_locaL", "Em mais de um município ou país"),
#     ]
#     onde_trabalha = models.CharField(max_length=25, choices=ONDE_TRABALHA_CHOICES, verbose_name="Em que município ou país estrangeiro trabalha?", blank=True, null=True)
#     estado_trabalho = models.CharField(max_length=25, verbose_name="Estado", blank=True, null=True)
#     municipio_trabalho = models.CharField(max_length=25, verbose_name="Município", blank=True, null=True)
#     pais_trabalho = models.CharField(max_length=25, verbose_name="País", blank=True, null=True)

#     RETORNA_3X_SEMANA_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     retorna_3x_semana = models.CharField(max_length=3, choices=RETORNA_3X_SEMANA_CHOICES, verbose_name="Retorna do trabalho para casa 3 dias ou mais na semana? (considerar a semana de 7 dias)", blank=True, null=True)

#     TEMPO_CASA_TRABALHO_CHOICES = (
#     [(str(horas), f"{horas} hora(s)") for horas in range(0, 25)] +
#     [(str(minutos), f"{minutos} minuto(s)") for minutos in range(0, 60)] +
#     [("nao_desloca", "Não se desloca para um local de trabalho")]
#     )
#     tempo_casa_trabalho = models.CharField(max_length=25, choices=TEMPO_CASA_TRABALHO_CHOICES, verbose_name="Quanto tempo leva entre sua casa e o local de trabalho normalmente?(Considerar o deslocamento casa-trabalho preferencialmente. Caso não seja possível, considerar o deslocamento de retorno (trabalho-casa))", blank=True, null=True)

#     MEIO_TRANSPORTE_TRABALHO_CHOICES = [
#     ("a_pe", "A pé"),
#     ("bicicleta", "Bicicleta"),
#     ("motocicleta", "Motocicleta"),
#     ("mototaxi", "Mototáxi"),
#     ("automovel", "Automóvel"),
#     ("taxi", "Táxi ou assemelhados"),
#     ("van", "Van, perua ou assemelhados"),
#     ("onibus", "Ônibus"),
#     ("pau_de_arara", "Caminhonete ou caminhão adaptado (pau de arara)"),
#     ("embarcacao_grande", "Embarcação de médio e grande porte (acima de 20 pessoas)"),
#     ("embarcacao_pequena", "Embarcação de pequeno porte (até 20 pessoas)"),
#     ("outros", "Outros"),
#     ]
#     meio_transporte_trabalho = models.CharField(max_length=25, choices=MEIO_TRANSPORTE_TRABALHO_CHOICES, verbose_name="Qual o principal meio de transporte utilizado para chegar ao local de trabalho? (Se utiliza vários meios de transporte, inclusive a pé, indique o que passa mais tempo.)", blank=True, null=True)

#     DIAGNOSTICO_AUTISMO_CHOICES = [
#     ("sim", "Sim"),
#     ("nao", "Não"),
#     ]
#     diagnostico_autismo = models.CharField(max_length=3, choices=DIAGNOSTICO_AUTISMO_CHOICES, verbose_name="Já foi diagnosticado(a) com autismo por algum profissional de saúde?", blank=True, null=True)

#     nome_contato = models.CharField(max_length=25, verbose_name="Nome do contato", blank=True, null=True)
#     email_contato = models.CharField(max_length=25, verbose_name="E-mail do contato", blank=True, null=True)
#     telefone_contato = models.CharField(max_length=25, verbose_name="Telefone do contato", blank=True, null=True)

#     religiao_ou_culto = models.CharField(max_length=100, verbose_name="Religião ou culto", blank=True, null=True)

