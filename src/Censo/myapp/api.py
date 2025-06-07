from rest_framework import viewsets
from myapp.models import Domicilio, Morador, IndentificacaoDeDomicilio, InformacoesMoradores
from myapp.serializers import DomicilioSerializer, MoradorSerializer, IndentificacaoDeDomicilioSerializer, IndentificacaoDeDomicilio, InformacoesMoradoresSerializer, InformacoesMoradores

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class IndentificacaoDeDomicilioViewSet(viewsets.ModelViewSet):
    queryset = IndentificacaoDeDomicilio.objects.all()
    serializer_class = IndentificacaoDeDomicilioSerializer

class InformacoesMoradoresViewSet(viewsets.ModelViewSet):
    queryset = InformacoesMoradores.objects.all()
    serializer_class = InformacoesMoradoresSerializer