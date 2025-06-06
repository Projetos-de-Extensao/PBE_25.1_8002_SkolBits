from rest_framework import viewsets
from myapp.models import IdentificacaoDomicilio, InformacoesMoradores, CaracteristicasDomicilio, CaracteristicasAdicionaisMoradores
from myapp.serializers import IdentificacaoDomicilioSerializer, InformacoesMoradoresSerializer, CaracteristicasDomicilioSerializer, CaracteristicasAdicionaisMoradoresSerializer

class IdentificacaoDomicilioViewSet(viewsets.ModelViewSet):
    queryset = IdentificacaoDomicilio.objects.all()
    serializer_class = IdentificacaoDomicilioSerializer

class InformacoesMoradoresViewSet(viewsets.ModelViewSet):
    queryset = InformacoesMoradores.objects.all()
    serializer_class = InformacoesMoradoresSerializer
class CaracteristicasDomicilioViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasDomicilio.objects.all()
    serializer_class = CaracteristicasDomicilioSerializer
class CaracteristicasAdicionaisMoradoresViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasAdicionaisMoradores.objects.all()
    serializer_class = CaracteristicasAdicionaisMoradoresSerializer