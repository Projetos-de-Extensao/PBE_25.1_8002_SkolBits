---
id: documento_de_visao
title: Documento de Visão
---

## Introdução

<p align="justify">
O presente documento tem como objetivo apresentar uma visão geral do projeto desenvolvido para a disciplina de Projeto Back-End, no contexto do Projeto de Extensão PBE_25.1_8002_SkolBits. O sistema consiste em uma aplicação web desenvolvida com Django e Python, com documentação via Swagger, que visa apoiar a comunidade da Ilha Primeira, no Rio de Janeiro, oferecendo um sistema de registro e análise de dados inspirado no modelo de coleta do IBGE.
</p>

## Descrição do Problema

<p align="justify">
A Ilha Primeira é uma comunidade que carece de dados organizados sobre seus moradores, condições de moradia, acesso a serviços e necessidades sociais. Essa ausência de informações dificulta a criação de políticas públicas, ações sociais e tomadas de decisão por parte de gestores e apoiadores da região.
</p>

### Problema

A inexistência de um sistema centralizado e acessível para registrar e consultar dados da comunidade da Ilha Primeira.

### Impactados

- Moradores da Ilha Primeira  
- Organizações sociais e comunitárias  
- Gestores públicos e apoiadores da região  
- Universidades e grupos de extensão envolvidos com a comunidade  

### Consequência

A falta de dados estruturados compromete o planejamento de ações sociais, a entrega de recursos e a criação de políticas públicas voltadas às reais necessidades dos moradores.

### Solução

A solução proposta é o desenvolvimento de uma aplicação web moderna que permita a coleta, o armazenamento e a visualização de dados relacionados aos domicílios, moradores e condições de vida na Ilha Primeira. A ferramenta será inspirada na metodologia do Censo do IBGE, mas com foco local e adaptada à realidade da comunidade.

## Objetivos

<p align="justify">
O principal objetivo do projeto é desenvolver uma plataforma funcional, segura e intuitiva que permita à equipe de campo, moradores e instituições parceiras acessar e registrar dados relevantes sobre a Ilha Primeira. Esses dados serão usados para criar relatórios, identificar demandas e propor soluções com base em evidências.
</p>

## Descrição do Usuário

<p align="justify">
Os usuários da plataforma serão os voluntários responsáveis pela coleta de dados, os moradores da Ilha Primeira com acesso permitido, e organizações parceiras. O sistema será acessado via navegador, com interface adaptada para dispositivos móveis, priorizando usabilidade, acessibilidade e segurança.
</p>

## Recursos do Produto

### Conta

<p align="justify">
Usuários autorizados poderão se cadastrar e fazer login para acessar o sistema, com permissões específicas conforme seu papel (coletor, administrador, visualizador).
</p>

### Cadastro de Domicílio

<p align="justify">
Permite o registro das informações de domicílios na Ilha Primeira, incluindo localização, estrutura da moradia e acesso a serviços básicos.
</p>

### Cadastro de Moradores

<p align="justify">
Permite o registro dos dados dos residentes, como idade, gênero, escolaridade, ocupação, religião, entre outros aspectos sociais.
</p>

### Relatórios e Análises

<p align="justify">
A aplicação permitirá gerar relatórios com filtros customizados, como faixa etária, educação ou situação de trabalho, oferecendo apoio à análise local.
</p>

### Documentação com Swagger

<p align="justify">
O backend da aplicação é documentado com Swagger, permitindo que desenvolvedores e mantenedores visualizem e testem os endpoints REST de forma prática.
</p>

## Restrições

<p align="justify">
A aplicação requer conexão com a internet para sincronização dos dados com o servidor. A coleta de dados será feita por pessoas treinadas e autorizadas. A privacidade dos dados será respeitada, com uso de criptografia e autenticação segura.
</p>

## Referências Bibliográficas

> Instituto Brasileiro de Geografia e Estatística (IBGE). Censo Demográfico 2022. Disponível em: https://censo2022.ibge.gov.br/. Acesso em: 09/06/2025  
> Django Project. Disponível em: https://www.djangoproject.com/  
> Swagger/OpenAPI Specification. Disponível em: https://swagger.io/specification/  

## Versionamento

| Data       | Versão | Descrição               | Autor(es)                       |
|------------|--------|--------------------------|----------------------------------|
| 09/06/2025 | 1.0    | Criação do documento     | Yago Duarte, Equipe SkolBits    |
