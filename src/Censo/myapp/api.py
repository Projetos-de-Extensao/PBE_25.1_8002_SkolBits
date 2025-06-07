from rest_framework import viewsets
from myapp.models import  IndentificacaoDeDomicilio, InformacoesMoradores, CaracteristicasDomicilio, RegistroCivil
from myapp.serializers import  IndentificacaoDeDomicilioSerializer, IndentificacaoDeDomicilio, InformacoesMoradoresSerializer,  CaracteristicasDomicilioSerializer, RegistroCivilSerializer


class IndentificacaoDeDomicilioViewSet(viewsets.ModelViewSet):
    queryset = IndentificacaoDeDomicilio.objects.all()
    serializer_class = IndentificacaoDeDomicilioSerializer

class InformacoesMoradoresViewSet(viewsets.ModelViewSet):
    queryset = InformacoesMoradores.objects.all()
    serializer_class = InformacoesMoradoresSerializer

class CaracteristicasDomicilioViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasDomicilio.objects.all()
    serializer_class = CaracteristicasDomicilioSerializer

class RegistroCivilViewSet(viewsets.ModelViewSet):
    queryset = RegistroCivil.objects.all()
    serializer_class = RegistroCivilSerializer
