from django.contrib import admin
from .models import IdentificacaoDomicilio, InformacoesMoradores, CaracteristicasDomicilio

admin.site.register(IdentificacaoDomicilio)
admin.site.register(InformacoesMoradores)
admin.site.register(CaracteristicasDomicilio)