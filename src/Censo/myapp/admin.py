from django.contrib import admin
from .models import IndentificacaoDeDomicilio,  InformacoesMoradores, CaracteristicasDomicilio


admin.site.register(InformacoesMoradores)
admin.site.register(CaracteristicasDomicilio)
admin.site.register(IndentificacaoDeDomicilio)  