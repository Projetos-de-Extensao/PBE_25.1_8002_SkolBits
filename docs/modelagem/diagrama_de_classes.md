---
id: diagrama_de_classes
title: Diagrama de Classes
---

# Não precisa entregar para a AP1
## Introdução

<p align = "justify">
O diagrama de classes UML é um diagrama que mostra a estrutura do sistema desenhado no nível de classes e interfaces, ilustra as funcionalidades, dependências e relacionamentos de cada elemento. Pode ser vista como uma representação visual da arquitetura de um sistema. 
</p>

## Metodologia

<p align = "justify">
A equipe se reuniu entre os dias 22/03 e 27/03 e realizou um brainstorm onde foram discutidos os tópicos-chave e a arquitetura geral dos sistemas, e assim criamos as primeiras ideias para a implementação.

Para a criação da primeira versão do diagrama de classes, Yago Duarte ficou responsável por todo o processo, com a ajuda de alguns participantes. Utilizou-se o programa [Miro] para a elaboração do diagrama. Além disso, a equipe utilizou o [Discord] para videoconferência.
</p>

# ENTREGUE NO PRÓXIMO INCREMENTO
## Diagrama de Classes

### Versão 1.0

![![Diagrama de Classes](../assets/diagrama_de_classes/diagrama_de_classes.png)](./Diagrama-UML-PBE-SkolBits.jpg)

### Versão 1.1

class Usuario:
    def __init__(self, id, nome, senha, email, nivel_acesso):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
        self.nivel_acesso = nivel_acesso

    def logar(self, email, senha):
        """Retorna True se o login for bem-sucedido, False caso contrário."""
        pass

    def logout(self):
        """Realiza o logout do usuário."""
        pass

    def verificar_permissao(self):
        """Verifica as permissões do usuário."""
        pass

    def recuperar_senha(self):
        """Envia um processo de recuperação de senha."""
        pass


class Autenticacao:
    def __init__(self, usuario_id, token, timestamp_expiracao):
        self.usuario_id = usuario_id
        self.token = token
        self.timestamp_expiracao = timestamp_expiracao

    def gerar_token(self, usuario_id):
        """Gera um token de autenticação para o usuário."""
        pass

    def validar_token(self, token):
        """Valida se o token ainda é válido."""
        pass

    def expirar_token(self):
        """Invalida o token atual."""
        pass


class Seguranca:
    def __init__(self, nivel_criptografia, logs, firewall):
        self.nivel_criptografia = nivel_criptografia
        self.logs = logs
        self.firewall = firewall

    def criptografar_dados(self, dado):
        """Aplica criptografia aos dados informados."""
        pass

    def validar_integridade(self):
        """Valida a integridade do sistema."""
        pass

    def auditar_logs(self):
        """Executa auditoria nos logs do sistema."""
        pass

    def ativar_firewall(self):
        """Ativa a proteção do firewall."""
        pass


class Backup:
    def __init__(self, frequencia_backup, ultimo_backup):
        self.frequencia_backup = frequencia_backup
        self.ultimo_backup = ultimo_backup

    def criar_backup(self):
        """Cria um novo backup dos dados."""
        pass

    def restaurar_backup(self):
        """Restaura o backup mais recente."""
        pass

    def verificar_integridade_backup(self):
        """Verifica se os backups estão íntegros e utilizáveis."""
        pass


class Domicilio:
    def __init__(self, id, endereco, tipo, num_comodos, tipo_moradia, estado, cidade, cadastro_ativo):
        self.id = id
        self.endereco = endereco
        self.tipo = tipo
        self.num_comodos = num_comodos
        self.tipo_moradia = tipo_moradia
        self.estado = estado
        self.cidade = cidade
        self.cadastro_ativo = cadastro_ativo

    def cadastrar_domicilio(self):
        """Registra um novo domicílio no sistema."""
        pass

    def editar_domicilio(self):
        """Edita informações de um domicílio já cadastrado."""
        pass

    def remover_domicilio(self):
        """Remove um domicílio do sistema."""
        pass


class Morador:
    def __init__(self, id, nome, idade, relacao, endereco, domicilio_id):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.relacao = relacao
        self.endereco = endereco
        self.domicilio_id = domicilio_id

    def adicionar_morador(self):
        """Adiciona um novo morador ao domicílio."""
        pass

    def editar_morador(self):
        """Edita informações de um morador cadastrado."""
        pass

    def remover_morador(self):
        """Remove um morador do domicílio."""
        pass


### Versão 2.0

![![Diagrama de Classes](../assets/diagrama_de_classes/diagrama_de_classes_1.1.png)](../assets/diagrama_de_classes/diagrama_de_classes_2.0.png)


#### Rastreabilidade de Requisitos

| ID|Descrição|
|---|---|
|US17, US18, US19, US20|Torneio|
|US01, US06, US07, US08|Usuário|
|US45|Rodada|
|US35|Partida|

## Conclusão

<p align = "justify">
Através do diagrama de classes, foi possível representar a estrutura do sistema a nível de classes e auxiliar na modelagem da arquitetura geral, além do banco de dados. Ao longo do desenvolvimento da disciplina, iremos adaptar e evoluir o diagrama e sua documentação para refletir no estado atual do projeto.
</p>

## Referências

> UML Class and Object Diagrams Overview. Disponível em https://www.uml-diagrams.org/class-diagrams-overview.html. Acesso em 21/09/20

## Autor(es)

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 27/03/2025 | 1.0 | Criação do documento | Yago Duarte |
