---
id: brainstorm
title: Brainstorm
---
 
## Introdução
<p align = "justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>
 
## Metodologia
<p align = "justify">
A equipe se reuniu para debater ideias gerais sobre o projeto via..., começou .... e terminou..., onde o XXXX XXXX foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.
</p>
 
## Brainstorm
 
## Versão 1.0
 
# Relatório de Brainstorm sobre Sistema de Cadastro de Moradores e Domicílios

## Participantes

1. **Fabricio de Brito**
2. **Lucas Kronemberger**
3. **Paco Guimaraes**
4. **Yago Duarte**
5. **Yuri Durra**

---

## Estrutura do Banco de Dados
- Definir quais tabelas serão utilizadas no banco de dados.
- Cada usuário deve possuir um ID único para identificação.
- Separar os dados de moradores e domicílios em tabelas distintas.
- Criar relacionamentos entre tabelas para evitar duplicação de informações.
- Escolher entre SQL ou NoSQL conforme a necessidade do projeto.
- Adicionar timestamps para rastrear a inserção e modificação dos dados.
- Criar índices em colunas frequentemente pesquisadas para melhorar o desempenho.

---

## Cadastro e Autenticação
- Definir o processo de login no sistema.
- Implementar níveis de acesso (admin, entrevistador, usuário comum).
- Utilizar tokens JWT para autenticação segura.
- Avaliar a necessidade de confirmação por e-mail no cadastro.
- Aplicar criptografia para proteger senhas e dados sensíveis.
- Considerar a implementação de login social (Google, Facebook, etc.).
- Oferecer autenticação multifator (MFA) para administradores.

---

## Rotas e API
- Criar rota para cadastrar um novo morador/domicílio.
- Criar rota para editar dados de um morador/domicílio.
- Criar rota para listar todos os moradores cadastrados.
- Criar rota para excluir um cadastro, caso necessário.
- Definir se as rotas serão públicas ou protegidas por autenticação.
- Padronizar os endpoints da API para facilitar integração.
- Implementar paginação na listagem de moradores para evitar sobrecarga no banco.
- Considerar o uso de GraphQL, caso seja necessária flexibilidade nas consultas.

---

## Regras de Negócio
- Impedir cadastros duplicados no sistema.
- Validar campos obrigatórios antes de salvar no banco.
- Garantir que os usuários só possam visualizar dados conforme seu nível de permissão.
- Definir limites de caracteres para campos como nome e endereço.
- Implementar logs de auditoria para registrar alterações nos dados.
- Criar um sistema de recuperação de senha seguro.
- Avaliar a necessidade de um sistema de denúncias ou feedback dentro do app.

---

## Segurança e Performance
- Evitar exposição de informações sensíveis nas respostas da API.
- Configurar CORS para controlar quais domínios podem acessar a API.
- Definir limites de requisição para evitar sobrecarga e ataques DDoS.
- Realizar testes de performance para garantir estabilidade da API sob alta demanda.
- Configurar um backup automático para evitar perda de dados.
- Armazenar dados de forma criptografada e segura.
- Implementar monitoramento ativo para identificar picos anormais de acesso.

 
### Requisitos elicitados
 
|ID|Descrição|
|----|-------------|
|BS01| O cliente...|
|BS02| O cliente...|
|BS03| O cliente...|
|BS04| O cliente...|
|BS05| O cliente...|
|BS06| O cliente...|
|BS07| O cliente...|
|BS08| O cliente...|
|BS09| O cliente...|
|BS10| O produto...|
|BS11| O produto...|
|BS12| O produto...|
|BS13| O produto...|
|BS14| O produto...|
|BS15| O produto...|
 
## Conclusão
<p align = "justify">
Através da aplicação da técnica, foi possível elicitar alguns dos primeiros requisitos do projeto.
</p>
## Referências Bibliográficas
 
> BARBOSA, S. D. J; DA SILVA, B. S. Interação humano-computador. Elsevier, 2010.
 
 
## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| DD/MM/YYYY | 1.0 | Criação do documento | XXX XXXX, XXXX XXXX, YYY YYYY e ZZZ XXXX |
