from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class indentificacao_domicilio(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=30)
    distrito = models.CharField(max_length=2)
    setor = models.CharField(max_length=4)
    nr_quadra = models.CharField(max_length=3)
    nr_da_face = models.CharField(max_length=3)

    def __str__(self):
        return self.uf
