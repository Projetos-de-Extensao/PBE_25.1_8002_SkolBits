from rest_framework import viewsets
from myapp.models import Domicilio, Morador
from myapp.serializers import DomicilioSerializer, MoradorSerializer, IndentificacaoDeDomicilioSerializer, IndentificacaoDeDomicilio

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class IndentificacaoDeDomicilioViewSet(viewsets.ModelViewSet):
    queryset = IndentificacaoDeDomicilio.objects.all()
    serializer_class = IndentificacaoDeDomicilioSerializer