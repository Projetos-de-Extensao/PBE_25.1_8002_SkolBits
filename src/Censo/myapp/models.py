from django.db import models
from enum import Enum
from django import forms


# Peguntas 1.1
class IdentificacaoDomicilio(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=30)
    distrito = models.CharField(max_length=2)
    setor = models.CharField(max_length=4)
    nr_quadra = models.CharField(max_length=3)
    nr_da_face = models.CharField(max_length=3)

    ESPECIE_CHOICES = [
        ('DPP', 'Domicílio particular permanente ocupado'),
        ('DPI', 'Domicílio particular improvisado ocupado'),
        ('DCM', 'Domicílio coletivo com morador'),
    ]
    tipo = models.CharField(max_length=3, choices=ESPECIE_CHOICES, default='DPP')


    def __str__(self):
        return f"Domicílio em {self.municipio}, UF: {self.uf}"
