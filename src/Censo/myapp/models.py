from django.db import models
from enum import Enum

class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro'
        NAO_INFORMADO = 'N', 'Prefiro não dizer'
    
class TipoRacial(models.TextChoices):
        BRANCA = 'BR', 'Branca'
        PRETA = 'PR', 'Preta'
        PARDA = 'PA', 'Parda'
        AMARELA = 'AM', 'Amarela'
        INDIGENA = 'IN', 'Indígena'
        NAO_INFORMADO = 'NI', 'Prefiro não dizer'
    
class Saneamento(models.TextChoices):
    REDE_PUBLICA = 'RP', 'Rede Pública'
    FOSSA = 'FS', 'Fossa'
    NENHUM = 'NN', 'Nenhum'

class Domicilio(models.Model):
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    tem_agua_encanada = models.BooleanField()
    tem_energia = models.BooleanField()
    tipo_esgoto = models.CharField(
        max_length=2,
        choices=Saneamento.choices
    )

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    raca_cor = models.CharField(max_length=2, choices=TipoRacial.choices)
    escolaridade = models.CharField(max_length=50)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='pessoas')
    
    def __str__(self):
        return self.nome
    
class Entregador(models.Model):
    STATUS_CHOICES = [
        ('DIS', 'Disponivel'),
        ('IND', 'Indisponivel'),
        ('ENT', 'Entregando'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='IND')
    cpf = models.CharField(max_length=11, unique=True)

class produto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    id_produto = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome 
    
class pedido (models.Model):
    STATUS_CHOICES = [
        ('PEN', 'Pendente'),
        ('APR', 'Aprovado'),
        ('CAN', 'Cancelado'),
    ]
    cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    entregador = models.ForeignKey(Entregador)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    data_pedido = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"
    
class pagamento (models.Model):
    STATUS_CHOICES = [
        ('PEN', 'Pendente'),
        ('APR', 'Aprovado'),
        ('CAN', 'Cancelado'),
    ]
    FORMA_CHOICES = [
        ('DIN', 'Dinheiro'),
        ('CAR', 'Cartão'),
        ('PIX', 'Pix'),
    ]
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    forma_pagamento = models.CharField(max_length=3, choices=FORMA_CHOICES, default='DIN')



